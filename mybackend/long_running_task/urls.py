from django.urls import path
from . import LongRunningTaskViews

urlpatterns = [
    path(
        "start-task/<str:image_id>/<int:task>",
        LongRunningTaskViews.LongRunningTaskCreateView.as_view(),
        name="start_long_running_task",
    ),
    path(
        "submit-tasks/<int:task>",
        LongRunningTaskViews.LongRunningTasksCreateView.as_view(),
        name="start_long_running_task",
    ),
    path(
        "get-progress/<str:task_id>/",
        LongRunningTaskViews.LongRunningTaskProgressView.as_view(),
        name="get_long_running_task_progress",
    ),
]
