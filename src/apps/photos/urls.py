from django.urls import path

from .views import gallery, upload_photo, view_photo

app_name = 'photos'

urlpatterns = [
    path('', gallery, name='gallery'),
    path('upload/', upload_photo, name='upload-photo'),
    path('photo/<int:pk>/', view_photo, name='view-photo'),
]
