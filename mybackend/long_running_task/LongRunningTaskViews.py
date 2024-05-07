from rest_framework.response import Response
from rest_framework import status
from .tasks import wait
from mybackend.celery import app as celery_app
from rest_framework.exceptions import ValidationError, NotFound
from long_running_task.api_responses.responses import (
    long_running_task_response,
    standard_response,
)
from datetime import datetime
from abc import ABC, abstractmethod
from mybackend.base_view import ImageView

         
class LongRunningTaskCreateView(ImageView):
    def post(self, request, image_id):
        try:
            image = self.image_services.get_image_by_id(image_id)

            task = wait.delay()
            
            return long_running_task_response(
                task_id=task.id,
                status= celery_app.AsyncResult(task.id).status,
                created_at=datetime.now(),
                location=f"http://127.0.0.1:8000/long_running_task/get-progress/{task.id}",
                status_code=status.HTTP_202_ACCEPTED,
            )
        except NotFound:
            return Response(
                {"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND
            )


class LongRunningTaskProgressView(ImageView):
    def get(self, request, task_id):
        task_result = celery_app.AsyncResult(task_id)
        response = {
            "task_id": task_id,
            "status": task_result.status,
        }

        if task_result.status == "PROGRESS":
            response.update(task_result.info)
        return Response(response, status=status.HTTP_200_OK)
