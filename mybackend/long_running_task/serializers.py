from rest_framework import serializers
from .models import TaskDBModel

class TaskAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskDBModel
        fields = [
            "id",
            "image_id",
            "status",
            "percentage",
            "result",
        ]
        extra_kwargs = {
            "result": {"required": False, "allow_blank": True},
        }
