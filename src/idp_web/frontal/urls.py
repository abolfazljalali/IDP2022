from django.urls import path
from . import views

app_name = 'frontal'
urlpatterns = [
    path('', views.image_list, name='image_list'),
    path('image/<int:image_id>/', views.image_by_id, name='image_by_id'),
    path('image/tag/<int:tag_id>/', views.image_by_tag, name='image_by_tag'),
]