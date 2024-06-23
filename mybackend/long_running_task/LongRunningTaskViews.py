from rest_framework.response import Response
from rest_framework import status
from mybackend.celery import app as celery_app
from rest_framework.exceptions import ValidationError, NotFound
from long_running_task.api_responses.responses import (
    long_running_task_response,
    standard_response,
)
from datetime import datetime
from abc import ABC, abstractmethod
from mybackendCommon.view.long_running_task_base_view import LongRunningTaskView
from .serializers import TaskAPISerializer, ImageIDsSerializer
import json
import pdb
"""
    Endpoint: http://127.0.0.1:8000/long_running_task/start-task/{image_id}/{task_number}
"""
class LongRunningTaskCreateView(LongRunningTaskView):
    def post(self, request, image_id, task):
        try:

            long_running_task = self.task_services.create_long_running_task(
                image_id, task
            )

            return long_running_task
        except NotFound:
            return Response(
                {"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND
            )

"""
    Endpoint: http://127.0.0.1:8000/long_running_task/submit-tasks/{task_number}
"""
class LongRunningTasksCreateView(LongRunningTaskView):
    def post(self, request,  task, *args, **kwargs):
        # pdb.set_trace()
        try:
            serializer = ImageIDsSerializer(data=request.data)
            print(serializer)
            if serializer.is_valid():
                image_ids = serializer.validated_data['image_ids']

                print(image_ids)
                responses = self.task_services.create_long_running_tasks(image_ids, task)
                print(responses)
                return Response(responses, status.HTTP_202_ACCEPTED)
            else:
                return Response({"message": "failed"}, status.HTTP_404_NOT_FOUND)
        except NotFound:
            return Response(
                {"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND
            )
"""
    Endpoint: http://127.0.0.1:8000/long_running_task/get-progress/{task_id}
"""
class LongRunningTaskProgressView(LongRunningTaskView):
    def get(self, request, task_id):
        try:
            
            task_api_model = self.task_services.get_task_progress_by_id(task_id)
            
            return Response(TaskAPISerializer(task_api_model).data, status.HTTP_200_OK)
            
        except NotFound:
            return Response(
                {"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND
            )
