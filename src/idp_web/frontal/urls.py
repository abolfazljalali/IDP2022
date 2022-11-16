from django.urls import path
from . import views

app_name = 'frontal'
urlpatterns = [
    path('', views.index, name='index'),
    path('image/<str:directory_path>/<str:file_name>/<int:file_type>', views.image_insert, name='image_insert'),
]