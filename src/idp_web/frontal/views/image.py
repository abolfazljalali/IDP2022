from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.core import serializers

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
    if request.method == 'POST':
        return HttpResponse(request.data)

    return HttpResponse(request.method)