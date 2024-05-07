import cv2
from abc import ABC, abstractmethod
from celery import Task

class BaseImageProcessingTask(ABC):
    name = 'detection_task'
    
    def __load_image(self, image):
        return cv2.imread( image )
    
    def __save_image(self, image, location):
        cv2.imwrite(location, image)
    
    @abstractmethod
    def run(self, image):
        raise NotImplementedError
    


class HumanDetection(BaseImageProcessingTask, Task):
    name = 'human_detection_task'
    
    def run(self, image_url):
        image = self.__load_image(image_url)
        
        hog = cv2.HOGDescriptor()
        
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

        (humans, _) = hog.detectMultiScale(image, winStride=(10, 10),
padding=(32, 32), scale=1.1)

        for (x, y, w, h) in humans:
            pad_w, pad_h = int(0.15 * w), int(0.01 * h)
            cv2.rectangle(image, (x + pad_w, y + pad_h), (x + w - pad_w, y + h - pad_h), (0, 255, 0), 2)
            
        print("Successfully detect human!")
        self.__save_image(image_url, "mybackend/media/")

'''
class AnimalDetection(BaseImageProcessingTask):
    def process(self, image_url):
        pass


'''

    