from django.urls import path
from . import views

urlpatterns = [
    path(
        "add-image/",
        views.ImageCreateView.as_view(),
        name="image_processing_add",
    ),
    path(
        "get-image/<str:image_id>/",
        views.ImageDetailView.as_view(),
        name="image_processing_get",
    ),
    path(
        "get-all-images/",
        views.ImageListView.as_view(),
        name="image_processing_get_all",
    ),
        path(
        "test/",
        views.ImageListView.as_view(),
        name="test",
    ),
]
