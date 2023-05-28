from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.vendedorSerializer import SellerSerializer
from authApp.models.vendedor import Seller

class SellerCreateView(views.APIView):
    def post(self, request,*args, **kwargs):
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status.HTTP_201_CREATED)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)