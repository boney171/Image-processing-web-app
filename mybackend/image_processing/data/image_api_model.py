from dataclasses import dataclass, field
from django.utils import timezone
from typing import Optional

@dataclass
class ImageAPIModel:
    id: int
    mime_type: str
    meta_width: int
    meta_height: int
    meta_size_byte: int
    file_path: Optional[str] = field(default=None)


