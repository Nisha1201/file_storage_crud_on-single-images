# image_app/urls.py
from django.urls import path
from .views import image_list, image_upload, image_update, image_delete

urlpatterns = [
    path('', image_list, name='image_list'),
    path('upload/', image_upload, name='image_upload'),
    path('update/<int:pk>/', image_update, name='image_update'),
    path('delete/<int:pk>/', image_delete, name='image_delete'),
]
