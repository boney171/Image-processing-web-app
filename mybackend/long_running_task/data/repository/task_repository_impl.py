from long_running_task.data.repository.task_repository import TaskRepository
from typing import List, Optional
from long_running_task.data.task_api_model import TaskAPIModel
from long_running_task.data.task_dto_model import TaskDTOModel
from long_running_task.models import TaskDBModel
from rest_framework.exceptions import NotFound
from datetime import datetime


class TaskRepositoryImpl(TaskRepository):

    def get(self, task_id) -> Optional[TaskDTOModel]:
            task_instance = TaskDBModel.objects.get(pk=task_id)

            return task_instance.to_dto(TaskDTOModel)
 

    def get_all(self) -> List[TaskDTOModel]:
        tasks = TaskDBModel.objects.all()

        task_dtos = []

        for task in tasks:
            task_dtos.append(task.to_dto(TaskDTOModel))

        return task_dtos

    def upsert(self, task_api_model: TaskAPIModel) -> TaskDTOModel:

        saved_task_instance, _ = TaskDBModel.objects.create_or_update(
            id=TaskAPIModel.id,
            defaults={
                "image_id": TaskAPIModel.image_id,
                "status": TaskAPIModel.status,
                "percentage": TaskAPIModel.percentage,
                "result": TaskAPIModel.result,
                "updated_at": datetime.now(),
            },
        )

        return saved_task_instance.to_dto(TaskDTOModel)

    def create(self, task_id, image_id, percentage, result) -> TaskDTOModel:
        
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