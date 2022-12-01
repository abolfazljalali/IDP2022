import os
import pathlib
import base64

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden, Http404
from django.shortcuts import render
from django.core import serializers
from django.conf import settings
from django.http import QueryDict

from tifffile import TiffFile
from PIL import Image
from io import BytesIO

from .. import models
from ..forms.image_upload import ImageUploadForm


@login_required(login_url='/admin/login/')
def image_list(request):
    '''
    Returns the list of all images available in the dataset.

            Parameters:
                    None

            Returns:
                    Model (Image): A serialized dict/json of the Image Model.
    '''

    try:
        retrieved_image = models.Image.objects.all()
        response_data = serializers.serialize('json', retrieved_image, fields=('pk', 'file_name','file_type', 'bands'))

    except models.Image.DoesNotExist:
        error_response = models.ErrorResponse()
        error_response.error_message = f'No data exists.'
        response_data = serializers.serialize('json', [error_response])

    return HttpResponse(response_data, content_type='application/json')


@login_required(login_url='/admin/login/')
def image_by_id(request, image_id):
    '''
    Returns the image corresponding to the primary key.

            Parameters:
                    image_id (int): A positive integer

            Returns:
                    Model (Image): A serialized dict/json of the Image Model.
    '''

    try:
        retrieved_image = models.Image.objects.get(pk=image_id)
        response_data = serializers.serialize('json', [retrieved_image], fields=('pk', 'file_name','file_type', 'bands'))

    except models.Image.DoesNotExist:
        error_response = models.ErrorResponse()
        error_response.error_message = f'The image with image_id:{image_id} does not exist.'
        response_data = serializers.serialize('json', [error_response])

    return HttpResponse(response_data, content_type='application/json')


@login_required(login_url='/admin/login/')
def image_by_tag(request, tag_id):
    '''
    Returns the images that relate to the tag id.

            Parameters:
                    tag_id (int): A positive integer

            Returns:
                    Model (Image): A serialized dict/json of the Image Model.
    '''

    try:
        retrieved_image = models.ImageTag.objects.filter(tag_id=tag_id)
        retrieved_image = [models.Image.objects.get(pk=image_id.id) for image_id in retrieved_image]
        response_data = serializers.serialize('json', retrieved_image)

    except models.Image.DoesNotExist:
        error_response = models.ErrorResponse()
        error_response.error_message = f'The images with tag_id:{tag_id} does not exist.'
        response_data = serializers.serialize('json', [error_response], fields=('error_message'))

    return HttpResponse(response_data, content_type='application/json')


@login_required(login_url='/admin/login/')
def image_preview(request, image_id, page_id):
    '''
    Returns the image corresponding to the primary key of the image, followed by its page number.
    If the page number is 0, then the RGB render of the image will be presented.

            Parameters:
                    image_id (int): A positive integer
                    page_id (int): A positive integer

            Returns:
                    Model (Image): A serialized dict/json of the Image Model.
    '''

    try:
        retrieved_image = models.Image.objects.get(pk=image_id)
        image_path = pathlib.Path(os.path.join(retrieved_image.directory_path, retrieved_image.file_name))

        with TiffFile(image_path) as tif_image:
            raw_img = tif_image.pages[page_id].asarray()
            img = None

            if page_id == 0:
                img = Image.fromarray(raw_img, 'RGB')
            else:
                img = Image.fromarray(raw_img, 'L')

            data = BytesIO()
            img.save(data, "JPEG") # pick your format
            data64 = base64.b64encode(data.getvalue())
            image_uri = u'data:img/jpeg;base64,'+data64.decode('utf-8')
            response_data = {'images':[{'img': image_uri, 'name':image_path.name}]}

        return render(request, 'frontal/index.html', response_data)

    except models.Image.DoesNotExist:
        error_response = models.ErrorResponse()
        error_response.error_message = f'The image with image_id:{image_id} does not exist.'
        response_data = serializers.serialize('json', [error_response])

    return HttpResponse(response_data, content_type='application/json')


@login_required(login_url='/admin/login/')
def image_insert(request):
    '''
    Inserts the image path and basic information to the database.

            Parameters:
                    file_name           (string): File name containing the format.
                    file                (bytes) : A file uploaded by user through a form as a post request.
                    * bands             (int)   : Number of channels that the image has. It is fed by the API during the insertion by inspecting into the image.
                    * directory_path    (string): A unix-based string path. Set by the specified MEDIA_ROOT.
                    * file_type         (int)   : File type or container is specified depending on the file suffix. Set during the insertion process.
                                        File type is followed by a code for quick access, for example: 
                                            - 100 for tiff.
                                            - 200 for jpeg.
                                            - 300 for png.
                    

            Returns:
                Success:
                    Model (OperationResult): A serialized dict/json of operation result beside the form.
                Fail:
                    Model (OperationResult): A serialized dict/json of operation result with the fail message.
    '''
    
    def handle_uploaded_file(file_full_path, file):
        with open(file_full_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

    def handle_uploaded_details(tif_img, image):

        for index, page in enumerate(tif_img.pages):
            first_page = models.Page()
            first_page.image = image
            first_page.page_number = index
            first_page.save()

            for tag in page.tags:
                tag_instance, _ = models.Tag.objects.get_or_create(name=tag.name)
                instance_tag = None

                if index == 0:
                    instance_tag = models.ImageTag()
                    instance_tag.image = image
                else:
                    instance_tag = models.PageTag(page=first_page)

                instance_tag.tag = tag_instance
                instance_tag.value = tag.value
                instance_tag.save()

    if not request.user.is_authenticated:
        print(request.user)

        return HttpResponseForbidden()
    
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)

        if form.is_valid():
            file_full_path = os.path.join(settings.IMAGE_FILE_DIR, request.POST['file_name'])
            handle_uploaded_file(file_full_path, request.FILES['file'])

            try:
                with TiffFile(file_full_path) as tiff_image:
                    file_format = pathlib.Path(file_full_path).suffix

                    new_image, created = models.Image.objects.get_or_create(
                        directory_path  = settings.IMAGE_FILE_DIR,
                        file_name       = request.POST['file_name'],
                        bands           = len(tiff_image.pages),
                        file_type       = models.FileFormat.objects.filter(value=file_format)[0])

                    if not created:
                        new_image.delete()
                        new_image = models.Image()

                    new_image.directory_path    = settings.IMAGE_FILE_DIR
                    new_image.file_name         = request.POST['file_name']
                    new_image.bands             = len(tiff_image.pages)
                    new_image.file_type         = models.FileFormat.objects.filter(value=file_format)[0]

                    new_image.save()
                    handle_uploaded_details(tiff_image, new_image)
                    form.clean()

            except Exception as e:

                if os.path.exists(file_full_path):
                    os.remove(file_full_path)
                    error_response = models.ErrorResponse()
                    error_response.error_message = f'Error while storing the information. Uploaded file was removed. Try again! \n{e}'
                    response_data = serializers.serialize('json', [error_response], fields=('error_message'))

                return HttpResponse(response_data, content_type='application/json')

            return render(request, 'frontal/image/upload.html', {'form': form, 'message':'Image was stored successfully.'})

        else:
            print(form.errors.as_data())

    else:
        form = ImageUploadForm()

    return render(request, 'frontal/image/upload.html', {'form': form})


@login_required(login_url='/admin/login/')
def image_update(request):
    '''
    Updates the image path and basic information in the database.

            Parameters:
                    image_id        (int)   : A bigint positive integer number.
                    directory_path  (string): A unix-based string path.
                    file_name       (string): File name containing the format.
                    file_type       (int)   : File type or container in form of an integer.
                                            
                                            - 0 for tiff.
                                            - 1 for jpeg.
                                            - 2 for png.

            Returns:
                    Model (OperationResult): A serialized dict/json of operation result.
    '''

    if not request.user.is_authenticated:
        return HttpResponseForbidden()

    if request.method == 'PUT':
        put = QueryDict(request.body)
        image_pk = int(put['image_id'])
        current_image = models.Image.objects.get(pk=image_pk)

        current_image.directory_path    = put['directory_path']
        current_image.file_name         = put['file_name']
        current_image.file_type         = int(put['file_type'])
        current_image.save()

        return HttpResponse('Data updated successfully.')

    return HttpResponse(request.method)


@login_required(login_url='/admin/login/')
def image_delete(request):
    '''
    Deletes the image in the database.

            Parameters:
                    image_id        (int)   : A bigint positive integer number.
            Returns:
                    Model (OperationResult): A serialized dict/json of operation result.
    '''

    if not request.user.is_authenticated:
        return HttpResponseForbidden()

    if request.method == 'DELETE':
        delete = QueryDict(request.body)

        image_pk = int(delete['image_id'])
        current_image = models.Image.objects.get(pk=image_pk)
        image_path = os.path.join(current_image.directory_path, current_image.file_name)

        if os.path.exists(image_path):
            os.remove(image_path)

        current_image.delete()
        return HttpResponse('Data deleted successfully.')

    return Http404()


@login_required(login_url='/admin/login/')
def image_download(request, image_id):
    '''
    Download the image in the database by image_id.

            Parameters:
                    image_id        (int)   : A bigint positive integer number.
            Returns:
                    Model (OperationResult): A serialized dict/json of operation result and downloadable content.
    '''
    if not request.user.is_authenticated:
        return HttpResponseForbidden()

    print(settings.MEDIA_ROOT)
    current_image = models.Image.objects.get(pk=image_id)
    print(os.path.join(current_image.directory_path, current_image.file_name))
    file_path = os.path.join(settings.IMAGE_FILE_DIR, current_image.file_name)
    print(os.path.exists(file_path))

    if os.path.exists(file_path):
        print(file_path)

        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="image/tiff")
            response['Content-Disposition'] = 'inline; filename=' + current_image.file_name.replace(' ', '_').replace(',', '-')

            return response

    raise Http404
