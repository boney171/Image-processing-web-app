import time
from kink import inject
from .models import TaskDBModel
from mybackend.celery import app as celery_app
import cv2
from kink import di, inject
import random
from long_running_task.data.task_api_model import TaskAPIModel
from mybackendCommon.tasks.task_interface import TaskInterface
from mybackendCommon.tasks.task_signal_interface import TaskSignalsInterface
from celery.signals import (
    task_success,
    task_failure,
    task_prerun,
    task_revoked
)
from long_running_task.data.repository.task_repository_impl import TaskRepositoryImpl
from image_processing.data.repository.image_repository_impl import ImageRepositoryImpl
from image_processing.utils.helpers import ImageUtils
import torch
from PIL import Image, ImageDraw

@inject
class HumanDetectingTask(TaskInterface):
    name = "human_detecting_task"
    max_retries = 3
    default_retry_delay = 10
    ignore_result = False
    
    def __init__(self, task_repository: TaskRepositoryImpl, image_repository : ImageRepositoryImpl, image_utils: ImageUtils):
        self.task_repository = task_repository
        self.image_repository = image_repository
        self.image_utils = image_utils
        
    def __update_progress_in_db(self, task_id):
        task_progress = celery_app.AsyncResult(task_id)
        
        task_instance = self.task_repository.get(task_id)

        progress_data_model = TaskAPIModel(
            id=task_id,
            image_id=task_instance.image_id,
            status=task_progress.status,
            percentage=task_progress.info["percent"],
            result=None,
        )
        self.task_repository.upsert(progress_data_model)
    
    def __get_model(self):
        return torch.hub.load('ultralytics/yolov5', 'yolov5s')
    
    def run(self, image_id, task, *args, **kwargs):
        try:
            total_steps = 10
            for i in range(1, total_steps + 1):
                time.sleep(1)
                percent_complete = (i / total_steps) * 100
                self.update_state(
                    state="PROGRESS", meta={"percent": f"{percent_complete:.0f}"}
                )
                self.__update_progress_in_db(self.request.id)

            image, file_path = self.image_utils.load_image(image_id)

            if image is None:
                raise ValueError(f"Failed to load image from path: {file_path}")

            model = self.__get_model()
            
            results = model(image)
            
            np_results = results.pandas().xyxy[0].to_numpy()
            
            detected_image = self.image_utils.draw_rectangulars(np_results, image, task, "Red", 2)

            self.image_utils.save_image(detected_image, file_path)
        except Exception as e:
            print(f"Error: {e}")


@inject
class ImageTaskSignals(TaskSignalsInterface):
    def __init__(self, task_repository: TaskRepositoryImpl, image_repository: ImageRepositoryImpl):
        # Dependency injection, let this class access database operation on tasks and images
        self.task_repository = task_repository
        self.image_repository = image_repository

        # Register before publish, after success and after failure signals
        task_prerun.connect(self.prerun_task)
        task_success.connect(self.on_task_success)
        task_failure.connect(self.on_task_failure)
        task_revoked.connect(self.on_task_revoked)

    def prerun_task(self, sender=None, task_id=None, task=None, *args, **kwargs):

        task_args = kwargs.get("args", [])

        image_id = task_args[0] if task_args else None
        
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

    def on_task_revoked(self, sender=None, request=None, terminated=None, signum=None, expired=None, **kwargs):
        if terminated:
            task_dto = self.task_repository.get(request.id)
            task_api = task_dto.to_api_model()
            task_api.status = "REVOKED"
            self.task_repository.upsert(task_api)

    

    
