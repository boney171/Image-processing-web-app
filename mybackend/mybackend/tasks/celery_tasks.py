from mybackend.celery import app as celery_app
from mybackend.di_container.bootstrap import bootstrap_di
from kink import di
from mybackend.tasks.base_task import ImageProcessingTask
from long_running_task.tasks import HumanDetectingTask

def register_tasks():
    celery_app.register_task(ImageProcessingTask(di["task_repository"], di["image_repository"]))
    celery_app.register_task(HumanDetectingTask(di["task_repository"], di["image_repository"]))