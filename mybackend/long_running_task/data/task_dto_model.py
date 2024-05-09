from dataclasses import dataclass
from datetime import datetime
from .task_api_model import TaskAPIModel

@dataclass
class TaskDTOModel:
    id: int
    status: str
    percentage: int
    result: str
    created_at: datetime
    updated_at: datetime

    def toAPIModel(self) -> TaskAPIModel:
        return TaskAPIModel(
            id=self.id,
            status=self.status,
            percentage=self.percentage,
            result=self.result,
        )
