from image_processing.data.image_api_model import ImageAPIModel
from .image_service import ImageService
from typing import List, Optional
from rest_framework.exceptions import NotFound
from rest_framework.exceptions import ValidationError
from uuid import uuid4
from image_processing.utils.helpers import save_file
from kink import inject


@inject
class ImageServiceImpl(ImageService):
    def __init__(self, image_repository):
        self.image_repository = image_repository

    def get_image_by_id(self, image_id) -> Optional[ImageAPIModel]:
        
        image_dto = self.image_repository.get(image_id)
        
        if image_dto is None:
            raise NotFound(f"No Image found with id: {image_id}")

        return image_dto.to_api_model()

    def get_all_images(self) -> List[ImageAPIModel]:
        
        image_dtos = self.image_repository.get_all()

        image_apis = []

        for dto in image_dtos:
            image_apis.append(dto.to_api_model())

        return image_apis

    def insert_image(self, image_data, file) -> ImageAPIModel:

        image_id = uuid4()

        file_path = save_file(file, image_id)

        image_dto = self.image_repository.create(
            ImageAPIModel(
                id=image_id,
                mime_type=image_data["mime_type"],
                meta_width=image_data["meta_width"],
                meta_height=image_data["meta_height"],
                meta_size_byte=image_data["meta_size_byte"],
                file_path=file_path,
            )
        )

        return image_dto.to_api_model()
