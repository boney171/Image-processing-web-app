from mybackend.celery import app as celery_app
from celery import Task
from kink import inject
import pdb
from celery.signals import (
    after_task_publish,
    task_success,
    task_failure,
    before_task_publish,
    task_prerun,
)
from datetime import datetime
from kink import di, inject
from long_running_task.data.task_api_model import TaskAPIModel
from rest_framework.exceptions import NotFound
from PIL import Image, ImageDraw

class ImageProcessingTask(Task):

    ignore_result = False
    name = "test_base_task"

    @inject
    def __init__(self, task_repository, image_repository):
        # Dependency injection, let this class access database operation on tasks and images
        self.task_repository = task_repository
        self.image_repository = image_repository

        # Register before publish, after success and after failure signals
        task_prerun.connect(self.prerun_task)
        task_success.connect(self.on_task_success)
        task_failure.connect(self.on_task_failure)

    def prerun_task(self, sender=None, task_id=None, task=None, *args, **kwargs):

        task_args = kwargs.get("args", [])

        image_id = task_args[0] if task_args else None
        
        print("Image instance: ", image_id)
        self.task_repository.create(task_id=task_id, image_id=image_id,percentage=0, result="null")

    def on_task_success(self, sender=None, result=None, **kwargs):

        try:
            task_dto = self.task_repository.get(sender.request.id)
            task_api = task_dto.to_api_model()
            image = self.image_repository.get(task_api.image_id)
            task_api.status = "SUCCESS"
            task_api.result = image.file_path
            self.task_repository.upsert(task_api)
        except self.task_repository.model.DoesNotExist:
            print(f"Task with id {sender.request.id} does not exist in the database.")

    def on_task_failure(self, sender=None, exception=None, **kwargs):
        try:
            task_dto = self.task_repository.get(sender.request.id)
            task_api = task_dto.to_api_model()
            task_api.status = "FAIL"
            self.task_repository.upsert(task_api)
        except self.task_repository.model.DoesNotExist:
            print(f"Task with id {sender.request.id} does not exist in the database.")

    def load_image(self, image_id):
        image_dto = self.image_repository.get(image_id)
        
        path = f"media/{image_dto.file_path}"
            
        return Image.open(path), path


    def save_image(self, image, location):
        image.save(location)

    def update_progress_in_db(self, task_id):
        task_progress = celery_app.AsyncResult(task_id)
        
        task_instance = self.task_repository.get(task_id)

        print("From update_progress_in_db: ", task_instance)
        print(task_instance.image_id)
        progress_data_model = TaskAPIModel(
            id=task_id,
            image_id=task_instance.image_id,
            status=task_progress.status,
            percentage=task_progress.info["percent"],
            result=None,
        )
        
        self.task_repository.upsert(progress_data_model)
    
    def draw_rectangular(self, x0,x1,y0,y1, image, color, width):
        draw = ImageDraw.Draw(image)
        
        draw.rectangle([x0, y0, x1, y1], outline=color, width=width)
        
        return draw
    def run(self, image_id, *args, **kwargs):
        pass
