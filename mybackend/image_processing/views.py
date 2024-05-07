from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageAPISerializer
from .serializers import ImageAPIDeserializer
from rest_framework.exceptions import ValidationError, NotFound
from mybackend.base_view import ImageView

class ImageDetailView(ImageView):
    def get(self, request, image_id):
        try:
            image_API_object = self.image_services.get_image_by_id(image_id)
            response = ImageAPISerializer(image_API_object)
            return Response(response.data, status=status.HTTP_200_OK)
        except NotFound: 
            return Response(
                {"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND
            )


class ImageListView(ImageView):
    def get(self, request):
        image_apis = self.image_services.get_all_images()
        response = ImageAPISerializer(image_apis, many=True)
        return Response(response.data, status=status.HTTP_200_OK)


class ImageCreateView(ImageView):
    def post(self, request):
        try:
            image_data = ImageAPIDeserializer(data=request.data)

            if image_data.is_valid(raise_exception=True):

                validated_data, file = image_data.separate_data()

                image_api_model = self.image_services.insert_image(validated_data, file)

                response = ImageAPISerializer(image_api_model)

                return Response(response.data, status=status.HTTP_201_CREATED)

        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"errors": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
