from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.core import serializers

from PIL import Image
import base64
from io import BytesIO


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
        retrived_mask = models.Mask.objects.all()
        response_data = serializers.serialize('json', retrived_mask)
    except models.Mask.DoesNotExist:
        errorResponse = models.ErrorResponse()
        errorResponse.error_message = f'No data exists.'
        response_data = serializers.serialize('json', [errorResponse])
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
        retrived_mask = models.Mask.objects.get(pk=mask_id)
        response_data = serializers.serialize('json', [retrived_mask])
    except models.Mask.DoesNotExist:
        errorResponse = models.ErrorResponse()
        errorResponse.error_message = f'The mask with mask_id:{mask_id} does not exist.'
        response_data = serializers.serialize('json', [errorResponse])
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
        retrived_mask = models.ImageMask.objects.filter(image_id=image_id)
        retrived_mask = [models.Mask.objects.get(pk=mask_id.id) for mask_id in retrived_mask]
        response_data = serializers.serialize('json', retrived_mask)
    except models.Image.DoesNotExist:
        errorResponse = models.ErrorResponse()
        errorResponse.error_message = f'The masks with image_id:{image_id} does not exist.'
        response_data = serializers.serialize('json', [errorResponse])
    return HttpResponse(response_data, content_type='application/json')

