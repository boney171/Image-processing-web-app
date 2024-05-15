from rest_framework.views import APIView
from kink import  inject
from abc import ABC, abstractmethod
from mybackend.di_container.bootstrap import bootstrap_di

@inject
class ImageView(APIView, ABC):
    def __init__(self, image_services):
        self.image_services = image_services
    
    def get(self):
        pass
    
    def post(self):
        pass