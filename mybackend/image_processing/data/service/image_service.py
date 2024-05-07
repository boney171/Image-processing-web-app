from abc import ABC, abstractmethod
from image_processing.data.ImageAPIModel import ImageAPIModel
from typing import List, Optional


class ImageService(ABC):
    @abstractmethod
    def get_image_by_id(self, image_id) -> Optional[ImageAPIModel]:
        raise NotImplementedError

    @abstractmethod
    def get_all_images(self) -> List[ImageAPIModel]:
        raise NotImplementedError

    @abstractmethod
    def insert_image(self, image_data, file) -> ImageAPIModel:
        raise NotImplementedError
