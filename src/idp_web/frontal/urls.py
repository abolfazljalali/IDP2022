from django.urls import path
from .views import image
from .views import mask

app_name = 'frontal'
urlpatterns = [
    # Image Model Routing
    path('image/', image.image_list, name='image_list'),
    path('image/<int:image_id>/', image.image_by_id, name='image_by_id'),
    path('image/tag/<int:tag_id>/', image.image_by_tag, name='image_by_tag'),
    path('image/insert', image.image_insert, name='image_insert'),
    path('image/update', image.image_update, name='image_update'),
    path('image/delete', image.image_delete, name='image_delete'),

    # Mask Model Routing
    path('mask/', mask.mask_list, name='mask_list'),
    path('mask/<int:mask_id>/', mask.mask_by_id, name='mask_by_id'),
    path('mask/image/<int:image_id>/', mask.mask_by_image_id, name='mask_by_image_id'),
]