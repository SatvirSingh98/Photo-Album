from django.shortcuts import get_object_or_404, redirect, render

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
    categories = Category.objects.all()
    if request.method == 'POST':
        category = None
        images = request.FILES.getlist('images')
        category_id = request.POST.get('category')
        new_category = request.POST.get('new_category')
        if category_id != 'none':
            category = Category.objects.get(id=category_id)
        elif new_category != '':
            category, _ = Category.objects.get_or_create(name=new_category.title())

        for image in images:
            Photo.objects.create(category=category, image=image)

        return redirect('/')

    context = {'categories': categories}
    return render(request, 'photos/upload_photo.html', context)
