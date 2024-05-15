from mybackendCommon.repository.base_repository import RepositoryAsset
from abc import ABC, abstractmethod
from typing import List, Optional
from long_running_task.data.task_api_model import TaskAPIModel
from long_running_task.data.task_dto_model import TaskDTOModel


class TaskRepository(RepositoryAsset, ABC):
    @abstractmethod
    def get(self, asset_id) -> Optional[TaskDTOModel]:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> List[TaskDTOModel]:
        raise NotImplementedError

    @abstractmethod
    def create(self, asset):
        raise NotImplementedError

    @abstractmethod
    def upsert(self, task_api_model: TaskAPIModel) -> TaskDTOModel:
        raise NotImplementedError

    def create(self, asset):
        pass
    
    def update(self, asset_id, update_info):
        pass

    def delete(self, asset_id):
        pass
