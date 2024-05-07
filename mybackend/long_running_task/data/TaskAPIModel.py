from dataclasses import dataclass, field
from django.utils import timezone
from typing import Optional


@dataclass
class TaskAPIModel:
    id: int
    status: str
    percentage: int
    result: Optional[str] = field(default=None)
