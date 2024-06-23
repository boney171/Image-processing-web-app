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

class ImageIDsSerializer(serializers.Serializer):
    image_ids = serializers.ListField(
        child=serializers.UUIDField(format='hex_verbose'),
        allow_empty=False
    )
    
class TaskResponseSerializer(serializers.Serializer):
    taskId = serializers.UUIDField(format='hex_verbose')
    status = serializers.CharField()
    imageId = serializers.CharField()
    createdAt = serializers.DateTimeField()
    location = serializers.URLField()