from mybackend.celery import app as celery_app
from mybackend.di_container.bootstrap import bootstrap_di
from kink import di
from long_running_task.tasks import HumanDetectingTask, ImageTaskSignals

def register_tasks():
    ''' Register Celery Tasks Here'''
    celery_app.register_task(HumanDetectingTask())
    
    ''' Register Signal Functions Here'''
    ImageTaskSignals()