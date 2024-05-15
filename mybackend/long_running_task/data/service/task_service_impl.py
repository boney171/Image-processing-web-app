from long_running_task.data.task_api_model import TaskAPIModel
from .task_service import TaskService
from typing import List, Optional
from rest_framework.exceptions import NotFound
from rest_framework.exceptions import ValidationError
from kink import inject
from datetime import datetime
from long_running_task.tasks import wait
from mybackend.celery import app as celery_app
from long_running_task.api_responses.responses import (
    long_running_task_response,
    standard_response,
)
from rest_framework import status

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
    
        image_dto = self.image_repository.get(image_id)

        
        if image_dto is None:
            raise NotFound(f"No Image found with id: {image_id}")
        
        
        long_running_task = wait.delay(image_id)
        
        return long_running_task_response(
                task_id=long_running_task.id,
                status= celery_app.AsyncResult(long_running_task.id).status,
                created_at=datetime.now(),
                location=f"http://127.0.0.1:8000/long_running_task/get-progress/{long_running_task.id}",
                status_code=status.HTTP_202_ACCEPTED,
            )
        