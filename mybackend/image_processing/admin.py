from django.contrib import admin
from image_processing.models import ImageDBModel


@admin.register(ImageDBModel)
class ImageDBAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "file_path",
        "mime_type",
        "meta_width",
        "meta_height",
        "created_at",
        "meta_size_byte",
    ]
