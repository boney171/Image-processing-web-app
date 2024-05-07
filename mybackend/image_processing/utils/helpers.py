from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def save_file(file, file_id):
    if file:
        file_name = f"media/{file_id}_{file.name}"
        saved_path = default_storage.save(file_name, ContentFile(file.read()))
        return saved_path
