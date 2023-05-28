from rest_framework import status, permissions, viewsets, views
from authApp.models.vendedor import Seller
from rest_framework.response import Response
from authApp.serializers.vendedorSerializer import SellerSerializer

class SellerDetailView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SellerSerializer

    def get(self, request, *args, **kwargs): 
        vendedor = Seller.objects.all()
        serializer = self.serializer_class(instance=vendedor,many=True)   
        return Response(serializer.data, status=status.HTTP_200_OK)