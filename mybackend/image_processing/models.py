from django.db import models
from django.utils import timezone
from uuid import uuid4
from .data.image_dto_model import ImageDTOModel
from django_dto import DTOMixin
# Create your models here.


class ImageDBModel(models.Model, DTOMixin):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    file_path = models.CharField(max_length=256, null=False, default="./images")
    created_at = models.DateTimeField(default=timezone.now)
    mime_type = models.CharField(
        max_length=50,
        choices=[("image/jpeg", "JPEG"), ("image/png", "PNG")],
        default="image/jpeg",
    )
    meta_width = models.IntegerField(null=False, default=5)
    meta_height = models.IntegerField(null=False, default=5)
    meta_size_byte = models.PositiveBigIntegerField(null=False, default=5)
