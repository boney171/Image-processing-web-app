from django.db import models
from django_dto import DTOMixin
from django.utils import timezone

class TaskDBModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    status = models.CharField(max_length=10, null=False, default="INQUEUE")
    percentage = models.IntegerField(null=False, default=0)
    location = models.CharField(max_length=100, default="http://127.0.0.1:8000/long_running_task/get-progress/{id}")
    result = models.CharField(max_length=100, null=True, default="http://127.0.0.1:8000/media/{location}")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    
    
