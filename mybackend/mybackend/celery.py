from __future__ import absolute_import, unicode_literals
import os
from long_running_task._tasks.BaseTask import HumanDetection
import multiprocessing
from celery import Celery
from django.conf import settings
from kink import di
import os
os.environ['OBJC_DISABLE_INITIALIZE_FORK_SAFETY'] = 'YES'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mybackend.settings')
multiprocessing.set_start_method('forkserver', force=True)
app = Celery('mybackend')



app.conf.enable_utc = True

app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

