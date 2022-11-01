from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from PIL import Image
import base64
from io import BytesIO


from . import models

# Create your views here.
def index(request):
    images = models.Image.objects.all().values()
    def to_data_uri(pil_img):
        data = BytesIO()
        pil_img.save(data, "JPEG") # pick your format
        data64 = base64.b64encode(data.getvalue())
        return u'data:img/jpeg;base64,'+data64.decode('utf-8')
    rendered_images = []
    for image in images:
        tags = []
        try:
            for tag in models.ImageTag.objects.filter(image=image['id']):
                tags.append(tag)
        except Exception as e:
            print(e)    
        rendered_images.append(
            {'name': image['file_name'],'img': to_data_uri(Image.open(f"{image['directory_path']}/{image['file_name']}")), 'tags': tags}
            )


    index_template = loader.get_template('frontal/index.html')
    context = {
        'images': rendered_images,
    }
    return HttpResponse(index_template.render(context, request))

