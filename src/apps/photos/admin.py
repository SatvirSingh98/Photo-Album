from django.contrib import admin

from .models import Category, Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date')


admin.site.register(Category)
