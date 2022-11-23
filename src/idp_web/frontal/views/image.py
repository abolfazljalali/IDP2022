import os
from django.http import HttpResponse, HttpResponseForbidden, Http404
from django.shortcuts import render
from django.template import loader
from django.core import serializers
from django.conf import settings
from django.http import QueryDict

from django.http import HttpResponseRedirect
from django.shortcuts import render
from ..forms.image_upload import ImageUploadForm


from PIL import Image
import base64
from io import BytesIO


from .. import models


def image_list(request):
    '''
    Returns the list of all images available in the dataset.

            Parameters:
                    None

            Returns:
                    Model (Image): A serialized dict/json of the Image Model.
    '''
    try:
        retrived_image = models.Image.objects.all()
        response_data = serializers.serialize('json', retrived_image)
    except models.Image.DoesNotExist:
        errorResponse = models.ErrorResponse()
        errorResponse.error_message = f'No data exists.'
        response_data = serializers.serialize('json', [errorResponse])
    return HttpResponse(response_data, content_type='application/json')


def image_by_id(request, image_id):
    '''
    Returns the image corresponding to the primary key.

            Parameters:
                    image_id (int): A positive integer

            Returns:
                    Model (Image): A serialized dict/json of the Image Model.
    '''
    try:
        retrived_image = models.Image.objects.get(pk=image_id)
        response_data = serializers.serialize('json', [retrived_image])
    except models.Image.DoesNotExist:
        errorResponse = models.ErrorResponse()
        errorResponse.error_message = f'The image with image_id:{image_id} does not exist.'
        response_data = serializers.serialize('json', [errorResponse])
    return HttpResponse(response_data, content_type='application/json')

def image_by_tag(request, tag_id):
    '''
    Returns the images that relate to the tag id.

            Parameters:
                    tag_id (int): A positive integer

            Returns:
                    Model (Image): A serialized dict/json of the Image Model.
    '''
    try:
        retrived_image = models.ImageTag.objects.filter(tag_id=tag_id)
        retrived_image = [models.Image.objects.get(pk=image_id.id) for image_id in retrived_image]
        response_data = serializers.serialize('json', retrived_image)
    except models.Image.DoesNotExist:
        errorResponse = models.ErrorResponse()
        errorResponse.error_message = f'The images with tag_id:{tag_id} does not exist.'
        response_data = serializers.serialize('json', [errorResponse])
    return HttpResponse(response_data, content_type='application/json')

def image_insert(request):
    '''
    Inserts the image path and basic information to the database.

            Parameters:
                    directory_path  (string): A unix-based string path.
                    file_name       (string): File name containing the format.
                    file_type       (int)   : File type or container in form of an integer.
                                            
                                            - 0 for tiff.
                                            - 1 for jpeg.
                                            - 2 for png.

            Returns:
                    Model (OperationResult): A serialized dict/json of operation result.
    '''
    def handle_uploaded_file(file_full_path, file):
        with open(file_full_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

    if not request.user.is_authenticated:
        print(request.user)
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_full_path = os.path.join(settings.IMAGE_FILE_DIR, request.POST['file_name'])
            handle_uploaded_file(file_full_path, request.FILES['file'])
            new_image = models.Image()
            new_image.directory_path    = settings.MEDIA_ROOT
            new_image.file_name         = request.POST['file_name']
            new_image.file_type         = int(request.POST['file_type'])
            new_image.save()
            return HttpResponse('NICE!')
        else:
            print(form.errors.as_data())
    else:
        form = ImageUploadForm()
    return render(request, 'frontal/image/upload.html', {'form': form})


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



def image_delete(request):
    '''
    Deletes the image in the database.

            Parameters:
                    image_id        (int)   : A bigint positive integer number.
            Returns:
                    Model (OperationResult): A serialized dict/json of operation result.
    '''
    print(request.user)
    
    if not request.user.is_authenticated:
        return HttpResponseForbidden()

    if request.method == 'DELETE':
        delete = QueryDict(request.body)

        image_pk = int(delete['image_id'])
        current_image = models.Image.objects.get(pk=image_pk)
        current_image.delete()
        return HttpResponse('Data deleted successfully.')

    return Http404()


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

    current_image = models.Image.objects.get(pk=image_id)
    file_path = os.path.join(current_image.directory_path, current_image.file_name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="image/tiff")
            response['Content-Disposition'] = 'inline; filename=' + current_image.file_name.replace(' ', '_').replace(',', '-')
            return response
    raise Http404


