"""
URL configuration for mybackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mybackend.di_container.bootstrap import bootstrap_di
from kink import di
from mybackend.celery import app as celery_app
from mybackend.tasks.base_task import ImageProcessingTask
from long_running_task.tasks import HumanDetectingTask
from celery.signals import after_task_publish, task_success, task_failure
from mybackend.tasks.celery_tasks import register_tasks

bootstrap_di()
register_tasks()

urlpatterns = [
    path('image_processing/', include('image_processing.urls')),
    path('long_running_task/', include("long_running_task.urls")),
    path('admin/', admin.site.urls),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)