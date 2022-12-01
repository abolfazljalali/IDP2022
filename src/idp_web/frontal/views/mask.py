from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.core import serializers
from django.http import HttpResponseForbidden
from django.conf import settings

import os
import base64
from io import BytesIO

from PIL import Image

from ..forms.mask_upload import MaskUploadForm
from .. import models


def mask_list(request):
    '''
    Returns the list of all masks available in the dataset.

            Parameters:
                    None

            Returns:
                    Model (Mask): A serialized dict/json of the Mask Model.
    '''
    
    try:
        retrieved_mask = models.Mask.objects.all()
        response_data = serializers.serialize('json', retrieved_mask)
        
    except models.Mask.DoesNotExist:
        error_response = models.ErrorResponse()
        error_response.error_message = f'No data exists.'
        response_data = serializers.serialize('json', [error_response])
        
    return HttpResponse(response_data, content_type='application/json')


def mask_by_id(request, mask_id):
    '''
    Returns the mask corresponding to the primary key.

            Parameters:
                    mask_id (int): A positive integer

            Returns:
                    Model (Mask): A serialized dict/json of the Mask Model.
    '''
    
    try:
        retrieved_mask = models.Mask.objects.get(pk=mask_id)
        response_data = serializers.serialize('json', [retrieved_mask])
        
    except models.Mask.DoesNotExist:
        error_response = models.ErrorResponse()
        error_response.error_message = f'The mask with mask_id:{mask_id} does not exist.'
        response_data = serializers.serialize('json', [error_response])
        
    return HttpResponse(response_data, content_type='application/json')


def mask_by_image_id(request, image_id):
    '''
    Returns the masks that relate to the image id.

            Parameters:
                    image_id (int): A positive integer

            Returns:
                    Model (Mask): A serialized dict/json of the Mask Model.
    '''

    try:
        retrieved_mask = models.ImageMask.objects.filter(image_id=image_id)
        retrieved_mask = [models.Mask.objects.get(pk=mask_id.id) for mask_id in retrieved_mask]
        response_data = serializers.serialize('json', retrieved_mask)

    except models.Image.DoesNotExist:
        error_response = models.ErrorResponse()
        error_response.error_message = f'The masks with image_id:{image_id} does not exist.'
        response_data = serializers.serialize('json', [error_response])

    return HttpResponse(response_data, content_type='application/json')


def mask_insert(request):
    '''
    Inserts the mask path and basic information to the database.

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
            print('file is writing')

            for chunk in file.chunks():
                destination.write(chunk)

    if not request.user.is_authenticated:
        print(request.user)

        return HttpResponseForbidden()
    
    if request.method == 'POST':
        form = MaskUploadForm(request.POST, request.FILES)

        if form.is_valid():
            file_full_path = os.path.join(settings.MEDIA_ROOT, request.POST['file_name'])
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
        form = MaskUploadForm()

    return render(request, 'frontal/image/upload.html', {'form': form})
