from celery import shared_task
import time
from datetime import datetime
from kink import inject


@shared_task(bind=True, task_track_started=True)
def wait(self):
    from .models import TaskDBModel
    from mybackend.celery import app as celery_app

    total_steps = 10
    for i in range(1, total_steps + 1):
        time.sleep(10)
        percent_complete = (i / total_steps) * 100
        self.update_state(
            state="PROGRESS", meta={"percent": f"{percent_complete:.0f}"}
        )

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


    
        