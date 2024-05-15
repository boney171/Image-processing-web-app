from celery import shared_task
from celery.signals import before_task_publish
from celery.signals import task_success
import time
from datetime import datetime
from kink import inject
from .models import TaskDBModel
from mybackend.celery import app as celery_app


def task_before_publish(headers, routing_key, **kwargs):

    task_id = headers.get("id")

    TaskDBModel.objects.update_or_create(
        id=task_id,
        defaults={
            "status": "INQUEUE",
            "percentage": 0,
            "location": f"http://127.0.0.1:8000/long_running_task/get-progress/{task_id}",
            "result": f"http://127.0.0.1:8000/media/",
            "created_at": datetime.now(),
        },
    )


before_task_publish.connect(task_before_publish)


@shared_task(bind=True, task_track_started=True)
def wait(self, *arg, **kwargs):

    
    total_steps = 10
    for i in range(1, total_steps + 1):
        time.sleep(10)
        percent_complete = (i / total_steps) * 100
        self.update_state(state="PROGRESS", meta={"percent": f"{percent_complete:.0f}"})

        task = celery_app.AsyncResult(self.request.id)
        task_entity, _ = TaskDBModel.objects.update_or_create(
            id=self.request.id,
            defaults={
                "status": task.status,
                "percentage": percent_complete,
                "location": f"http://127.0.0.1:8000/long_running_task/get-progress/{self.request.id}",
                "result": f"http://127.0.0.1:8000/media/{task.status}",
                "updated_at": datetime.now(),
            },
        )
    return "Done"


def on_task_success(sender=None, result=None, **kwargs):

    task_id = sender.request.id
    TaskDBModel.objects.update_or_create(
        id=task_id,
        defaults={
            "status": "SUCCESS",
            "percentage": 100,
            "location": f"http://127.0.0.1:8000/long_running_task/get-progress/task_id",
            "result": f"http://127.0.0.1:8000/media/Success",
            "updated_at": datetime.now(),
        },
    )
    print(f"Task {sender.name} with ID {sender.request.id} was successful.")
    print(f"Result: {result}")


task_success.connect(on_task_success)


# Step to create iomplement different task

# How to create my own task

# How to submit multiple jobs

# Use debugger

# Run celery as debugger
