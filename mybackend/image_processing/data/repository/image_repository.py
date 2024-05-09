
from mybackendCommon.repository.base_repository import RepositoryAsset
from abc import ABC, abstractmethod
from typing import List, Optional
from image_processing.data.image_dto_model import ImageDTOModel
from image_processing.data.image_api_model import ImageAPIModel

class ImageRepository(RepositoryAsset, ABC):
    @abstractmethod
    def get(self, asset_id) -> Optional[ImageDTOModel]:
        pass
    
    @abstractmethod
    def get_all(self) -> List[ImageDTOModel]:
        pass
    
    @abstractmethod
    def create(self, image_api_model:ImageAPIModel)->ImageDTOModel:
        pass
    
    def update(self, asset_id, update_info):
        pass
    
    def delete(self, asset_id):
        pass