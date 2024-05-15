from django.contrib import admin
from image_processing.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "image_id",
        "file_path",
        "mime_type",
        "meta_width",
        "meta_height",
        "created_at",
    ]
