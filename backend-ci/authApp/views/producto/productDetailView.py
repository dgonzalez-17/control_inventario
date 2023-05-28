from itertools import product
from rest_framework import status, permissions, viewsets, views
from authApp.models.product import Product
from rest_framework.response import Response
from authApp.serializers.productoSerializer import ProductSerializer

class ProductDetailView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs): 
        product = Product.objects.all()
        serializer = self.serializer_class(instance=product,many=True)   
        return Response(serializer.data, status=status.HTTP_200_OK)
        