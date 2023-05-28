from rest_framework import status,views
from rest_framework.response import Response
from authApp.serializers.productoSerializer import ProductSerializer
from authApp.models.product import Product

class ProductCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializers = ProductSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(status.HTTP_201_CREATED)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)