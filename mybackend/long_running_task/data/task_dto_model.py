from dataclasses import dataclass
from datetime import datetime
from .task_api_model import TaskAPIModel

@dataclass
class TaskDTOModel:
    id: int
    image_id: int
    status: str
    percentage: int
    result: str
    created_at: datetime
    updated_at: datetime

    def to_api_model(self) -> TaskAPIModel:
        return TaskAPIModel(
            id=self.id,
            image_id=self.image_id,
            status=self.status,
            percentage=self.percentage,
            result=self.result,
        )
