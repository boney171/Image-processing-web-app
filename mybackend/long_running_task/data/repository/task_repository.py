from mybackendCommon.repository.base_repository import RepositoryAsset
from abc import ABC, abstractmethod
from typing import List, Optional
from long_running_task.data.task_api_model import TaskAPIModel
from long_running_task.data.task_dto_model import TaskDTOModel


class TaskRepository(RepositoryAsset, ABC):
    @abstractmethod
    def get(self, asset_id) -> Optional[TaskDTOModel]:
        pass

    @abstractmethod
    def upsert(self, task_api_model: TaskAPIModel) -> TaskDTOModel:
        pass

    @abstractmethod
    def delete(self, asset_id):
        pass
