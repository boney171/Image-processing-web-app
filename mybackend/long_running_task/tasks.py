import time
from datetime import datetime
from kink import inject
from .models import TaskDBModel
from mybackend.celery import app as celery_app
from mybackend.tasks.base_task import ImageProcessingTask
import cv2
from kink import di, inject
import random
from PIL import Image, ImageDraw
import numpy as np



class HumanDetectingTask(ImageProcessingTask):
    name = "human_detecting_task"
    max_retries = 3
    default_retry_delay = 10
    
    def __init__(self, task_repository, image_repository):
        super().__init__(task_repository, image_repository)

    
    
    def run(self, image_id, *args, **kwargs):
        try:
            total_steps = 10
            for i in range(1, total_steps + 1):
                time.sleep(5)
                percent_complete = (i / total_steps) * 100
                self.update_state(
                    state="PROGRESS", meta={"percent": f"{percent_complete:.0f}"}
                )
                self.update_progress_in_db(self.request.id)

            image, file_path = self.load_image(image_id)

            if image is None:
                raise ValueError(f"Failed to load image from path: {file_path}")

            width, height = image.size
            self.draw_rectangular(
                random.randint(0, width // 2),
                random.randint(width // 2, width),
                random.randint(0, height // 2),
                random.randint(height // 2, height),
                image,
                "black",
                5,
            )

            self.save_image(image, file_path)
        except Exception as e:
            print(f"Error: {e}")

        return "Done"


