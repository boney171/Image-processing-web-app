from rest_framework import serializers
from .models import ImageDBModel
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


class ImageAPIDeserializer(serializers.ModelSerializer):
    file = serializers.FileField(write_only=True)

    class Meta:
        model = ImageDBModel
        fields = [
            "file_path",
            "created_at",
            "mime_type",
            "meta_width",
            "meta_height",
            "meta_size_byte",
            "file",
        ]
        extra_kwargs = {
            "mime_type": {"required": True, "allow_blank": False},
            "file": {"required": True, "allow_blank": False},
        }

    def separate_data(self):
        validated_data = self.validated_data

        file = validated_data.pop("file")

        return validated_data, file


class ImageAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageDBModel
        fields = [
            "id",
            "file_path",
            "mime_type",
            "meta_width",
            "meta_height",
            "meta_size_byte",
        ]
