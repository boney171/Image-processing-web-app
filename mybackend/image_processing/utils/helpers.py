from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from mybackend.celery import app as celery_app
from celery import Task
from kink import inject
from datetime import datetime
from kink import di, inject
from long_running_task.data.task_api_model import TaskAPIModel
from rest_framework.exceptions import NotFound
from PIL import Image, ImageDraw
import numpy as np
from image_processing.data.repository.image_repository_impl import ImageRepositoryImpl
def save_file(file, file_id):
    if file:
        file_name = f"media/{file_id}_{file.name}"
        saved_path = default_storage.save(file_name, ContentFile(file.read()))
        return saved_path

@inject
class ImageUtils():
    
    def __init__(self, image_repository: ImageRepositoryImpl) -> None:
        self.image_repository = image_repository
        
    def load_image(self, image_id):
        image_dto = self.image_repository.get(image_id)
        
        path = f"media/{image_dto.file_path}"
        
        
        return Image.open(path), path
    
    def save_image(self, image, location):
        image.save(location)
    
        
    def draw_rectangulars(self, results, image, category, color, width):  
        draw = ImageDraw.Draw(image)  
        for res in results:
            xmin, ymin, xmax, ymax, confidence, class_id, class_name = res
            if class_name == category:
                draw.rectangle([int(xmin), int(ymin), int(xmax), int(ymax)], outline=color, width=width)
        return image 

    