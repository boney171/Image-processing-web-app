from long_running_task.data.repository.task_repository import TaskRepository
from typing import List, Optional
from long_running_task.data.task_api_model import TaskAPIModel
from long_running_task.data.task_dto_model import TaskDTOModel
from long_running_task.models import TaskDBModel
from rest_framework.exceptions import NotFound

class TaskRepositoryImpl(TaskRepository):
    
    def get(self, asset_id) -> Optional[TaskDTOModel]:
        pass

    
    def upsert(self, task_api_model: TaskAPIModel) -> TaskDTOModel:
        pass

    
    def delete(self, asset_id):
        pass
