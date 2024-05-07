from django.contrib import admin
from image_processing.models import ImageDBModel
from long_running_task.models import TaskDBModel

@admin.register(TaskDBModel)
class TaskDBAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "status",
        "percentage",
        "location",
        "result",
        "created_at",
        "updated_at",
    ]
