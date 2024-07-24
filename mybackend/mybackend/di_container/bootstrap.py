
from kink import di
from image_processing.data.repository.image_repository_impl import ImageRepositoryImpl
from image_processing.data.service.image_service_impl import ImageServiceImpl
from long_running_task._tasks.BaseTask import HumanDetection
from long_running_task.data.repository.task_repository_impl import TaskRepositoryImpl
from long_running_task.data.service.task_service_impl import TaskServiceImpl
from long_running_task.tasks import ImageTaskSignals
from image_processing.utils.helpers import ImageUtils
from long_running_task.tasks import HumanDetectingTask
def bootstrap_di() -> None:
    di["image_repository"] = ImageRepositoryImpl()
    di["image_services"] = ImageServiceImpl(di["image_repository"])
    
    di["task_repository"] = TaskRepositoryImpl()
    di["task_services"] = TaskServiceImpl( di["task_repository"], di["image_repository"])

    di["image_utils"] = ImageUtils()
    di["image_signals"] = ImageTaskSignals()
    di["human_detecting_task"] = HumanDetectingTask()
        