from dataclasses import dataclass, field
from datetime import datetime
from .ImageAPIModel import ImageAPIModel
from typing import Optional

@dataclass
class ImageDTOModel:
    id: int
    file_path: str
    mime_type: str
    meta_width: int
    meta_height: int
    meta_size_byte: int
    created_at: datetime

    def toAPIModel(self) -> ImageAPIModel:
        return ImageAPIModel(
            id=self.id,
            file_path=self.file_path,
            mime_type=self.mime_type,
            meta_width=self.meta_width,
            meta_height=self.meta_height,
            meta_size_byte=self.meta_size_byte,
        )
