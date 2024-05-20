from mybackend.celery import app as celery_app
from celery import Task
from kink import inject
from celery.signals import (
    after_task_publish,
    task_success,
    task_failure,
    before_task_publish,
    task_prerun,
)
from datetime import datetime
from kink import di, inject
import time
from long_running_task.data.task_api_model import TaskAPIModel


class ImageProcessingTask(Task):

    ignore_result = False
    name = "test_base_task"

    def __init__(self, task_repository, image_repository):
        # Dependency injection, let this class access database operation on tasks and images
        self.task_repository = task_repository
        self.image_dto = image_repository

        # Register before publish, after success and after failure signals
        task_prerun.connect(self.prerun_task)
        task_success.connect(self.on_task_success)
        task_failure.connect(self.on_task_failure)

    def prerun_task(self, sender=None, task_id=None, task=None, *args, **kwargs):

        task_args = kwargs.get("args", [])
        
        image_id = task_args[0] if task_args else None

        self.task_repository.create(task_id, None, 0, "null")

    def on_task_success(self, sender=None, result=None, **kwargs):

        task_dto = self.task_repository.get(sender.request.id)

        task_api = task_dto.to_api_model()
        
        task_api.status = "SUCCESS"

        self.task_repository.upsert(task_api)
        

    def on_task_failure(self, sender=None, exception=None, **kwargs):

        task_dto = self.task_repository.get(sender.request.id)

        task_api = task_dto.to_api_model()
        
        task_api.status = "FAIL"

        self.task_repository.upsert(task_api)
    
    def run(self, image_id, *args, **kwargs):
        total_steps = 10

        for i in range(1, total_steps + 1):
            time.sleep(10)
            percent_complete = (i / total_steps) * 100
            self.update_state(
                state="PROGRESS", meta={"percent": f"{percent_complete:.0f}"}
            )

            task_progress = celery_app.AsyncResult(self.request.id)

            self.task_repository.upsert(
                TaskAPIModel(
                    id=task_progress.id,
                    image_id=None,
                    status=task_progress.status,
                    percentage=task_progress.info["percent"],
                    result=None,
                )
            )

        return "Done"
