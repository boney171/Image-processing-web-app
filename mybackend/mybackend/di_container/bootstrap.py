
from kink import di
from image_processing.data.repository.image_repositoryImpl import ImageRepositoryImpl
from image_processing.data.service.image_serviceImpl import ImageServiceImpl
from long_running_task._tasks.BaseTask import HumanDetection
#from long_running_task._tasks.BaseTask import AnimalDetection
def bootstrap_di() -> None:
    di["image_repository"] = ImageRepositoryImpl()
    di["image_services"] = ImageServiceImpl(di["image_repository"])
    di["human_detection_operator"] = HumanDetection()
