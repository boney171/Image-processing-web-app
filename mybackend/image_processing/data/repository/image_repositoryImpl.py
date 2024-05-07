from image_processing.data.repository.image_repository import ImageRepository
from image_processing.serializers import ImageAPISerializer
from image_processing.serializers import ImageAPIDeserializer
from typing import List, Optional
from image_processing.data.ImageDTOModel import ImageDTOModel
from image_processing.data.ImageAPIModel import ImageAPIModel
from image_processing.models import ImageDBModel
from rest_framework.exceptions import ValidationError
from rest_framework.exceptions import NotFound


class ImageRepositoryImpl(ImageRepository):
    def get(self, image_id) -> Optional[ImageDTOModel]:
        try:
            image_instance = ImageDBModel.objects.get(pk=image_id)

            return image_instance.to_dto(ImageDTOModel)
        
        except ImageDBModel.DoesNotExist:
            raise NotFound(f"No Image found with id: {image_id}")

    def get_all(self) -> List[ImageDTOModel]:
        images = ImageDBModel.objects.all()

        image_dtos = []

        for image in images:
            image_dtos.append(
                image.to_dto(ImageDTOModel)
            )
        return image_dtos

    def create(self, image_api_model: ImageAPIModel) -> ImageDTOModel:

        image_instance = ImageDBModel(
            id=image_api_model.id,
            mime_type=image_api_model.mime_type,
            meta_width=image_api_model.meta_width,
            meta_height=image_api_model.meta_height,
            meta_size_byte=image_api_model.meta_size_byte,
            file_path=image_api_model.file_path,
        )
        image_instance.save()

        saved_image_instance = ImageDBModel.objects.get(pk=image_api_model.id)

        return saved_image_instance.to_dto(ImageDTOModel)

    def update(self, image_id, update_info):
        pass

    def delete(self, image_id):
        pass
