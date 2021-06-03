from django.shortcuts import get_object_or_404, render

from .models import Category, Photo


def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)


def view_photo(request, pk=None):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'photos/view_photo.html', {'photo': photo})


def upload_photo(request):
    return render(request, 'photos/upload_photo.html')
