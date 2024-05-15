from abc import ABC, abstractmethod
from long_running_task.data.task_api_model import TaskAPIModel
from typing import List, Optional


class TaskService(ABC):

    @abstractmethod
    def get_progress_by_id(self, task_id):
        raise NotImplementedError
    
    @abstractmethod
    def get_all_tasks(self) -> List[TaskAPIModel]:
        raise NotImplementedError
    
    @abstractmethod
    def create_long_running_task(self, image_id, task):
        raise NotImplementedError
