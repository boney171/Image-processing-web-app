from long_running_task.data.repository.task_repository import TaskRepository
from typing import List, Optional
from long_running_task.data.task_api_model import TaskAPIModel
from long_running_task.data.task_dto_model import TaskDTOModel
from long_running_task.models import TaskDBModel
from rest_framework.exceptions import NotFound
from datetime import datetime
from django.db import transaction


class TaskRepositoryImpl(TaskRepository):

    def get(self, task_id) -> Optional[TaskDTOModel]:
        with transaction.atomic():    
            task_instance = TaskDBModel.objects.get(pk=task_id)

            return task_instance.to_dto(TaskDTOModel)
 

    def get_all(self) -> List[TaskDTOModel]:
        with transaction.atomic():    
            tasks = TaskDBModel.objects.all()

        task_dtos = []

        for task in tasks:
            task_dtos.append(task.to_dto(TaskDTOModel))

        return task_dtos

    def upsert(self, task_api_model: TaskAPIModel) -> TaskDTOModel:
        with transaction.atomic():    
            saved_task_instance, _ = TaskDBModel.objects.update_or_create(
                id=task_api_model.id,
                defaults={
                    "image_id": task_api_model.image_id,
                    "status": task_api_model.status,
                    "percentage": task_api_model.percentage,
                    "result": task_api_model.result,
                    "updated_at": datetime.now(),
                },
             )

        return saved_task_instance.to_dto(TaskDTOModel)

    def create(self, task_id, image_id, percentage, result) -> TaskDTOModel:
        with transaction.atomic():   
            saved_task = TaskDBModel.objects.create(
                id = task_id,
                image_id = image_id,
                percentage = percentage,
                result = result,
                created_at = datetime.now()
            )
        
        return saved_task.to_dto(TaskAPIModel)
    
    def delete(self, asset_id):
        pass
        
    def update(self, asset_id, update_info):
        pass