from long_running_task.data.task_api_model import TaskAPIModel
from .task_service import TaskService
from typing import List, Optional
from rest_framework.exceptions import NotFound
from rest_framework.exceptions import ValidationError
from kink import inject
from datetime import datetime
from mybackend.tasks.base_task import ImageProcessingTask
from mybackend.celery import app as celery_app
from long_running_task.api_responses.responses import (
    long_running_task_response,
    long_running_tasks_response,
    standard_response,
)
from rest_framework import status
import pdb
import uuid
@inject
class TaskServiceImpl(TaskService):
    def __init__(self, task_repository, image_repository):
        self.task_repository = task_repository
        self.image_repository = image_repository
        
    
    def get_task_progress_by_id(self, task_id) -> Optional[TaskAPIModel]:
        
        task_dto = self.task_repository.get(task_id)
        
        if task_dto is None:
            raise NotFound(f"No Task found with id: {task_id}")
        
        return task_dto.to_api_model()
    
    def get_all_tasks(self) -> List[TaskAPIModel]:
        
        task_dtos = self.task_repository.get_all()
        
        task_apis = []
        
        for dto in task_dtos:
            task_apis.append(dto.to_api_model())
        
        return task_apis
            

    def get_progress_by_id(self, task_id):
        pass
    
    def create_long_running_task(self, image_id, task):
        
        print("Task ", task)
        
        image_dto = self.image_repository.get(image_id)

        if image_dto is None:
            raise NotFound(f"No Image found with id: {image_id}")
        
        long_running_task = celery_app.tasks['human_detecting_task']
        
        task = long_running_task.delay(image_id)
        
        return long_running_task_response(
                task_id=task.id,
                status= celery_app.AsyncResult(task.id).status,
                created_at=datetime.now(),
                location=f"http://127.0.0.1:8000/long_running_task/get-progress/{task.id}",
                status_code=status.HTTP_202_ACCEPTED,
            )
    
    def create_long_running_tasks(self, image_ids, task):
        tasks_responses = []
        wait = 0

        print(image_ids)
        for image_id in image_ids:
            image_uuid = uuid.UUID(str(image_id))

            image_dto = self.image_repository.get(image_uuid)
            if image_dto is None:
                raise NotFound(f"No Image found with id: {image_uuid}")

            long_running_task = celery_app.tasks['human_detecting_task']
            task_result = long_running_task.apply_async(args=[image_uuid], countdown=wait)

            task_response = {
                "taskId": task_result.id,
                "status": celery_app.AsyncResult(task_result.id).status,
                "imageId": str(image_uuid),
                "createdAt": datetime.now(),
                "location": f"http://127.0.0.1:8000/long_running_task/get-progress/{task_result.id}",
            }

            tasks_responses.append(task_response)
            wait += 0

        return tasks_responses
        
    def stop_long_running_task(self, task_id):
        task_dto = self.task_repository.get(task_id)
        
        if task_dto is None:
            raise NotFound(f"No task found with id: {task_id}")
        
        celery_app.control.revoke(task_id, terminate=True)
        