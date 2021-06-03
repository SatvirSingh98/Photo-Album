from django.shortcuts import render


def gallery(request):
    return render(request, 'photos/gallery.html')


def view_photo(request, pk=None):
    return render(request, 'photos/view_photo.html')


def upload_photo(request):
    return render(request, 'photos/upload_photo.html')
