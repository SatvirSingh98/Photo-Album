from django.urls import path

from .views import gallery, upload_photo, view_photo

app_name = 'photos'

urlpatterns = [
    path('', gallery, name='home'),
    path('upload/', upload_photo, name='home'),
    path('photo/<int:pk>/', view_photo, name='home'),
]
