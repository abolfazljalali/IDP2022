from django.contrib import admin
from . import models


admin.site.register(models.Image)
admin.site.register(models.Annotation)
admin.site.register(models.Color)
admin.site.register(models.ImageTag)
admin.site.register(models.ImageMask)
admin.site.register(models.Mask)
admin.site.register(models.Polygon)
admin.site.register(models.Segment)
admin.site.register(models.SegmentTag)
admin.site.register(models.Tag)
