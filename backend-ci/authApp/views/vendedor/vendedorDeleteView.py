from rest_framework import status, permissions, viewsets, views
from authApp.models.vendedor import Seller
from rest_framework.response import Response
from authApp.serializers.vendedorSerializer import SellerSerializer
import json 

class SellerDeleteView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SellerSerializer

    def delete(self, request,seller_id,):
        vendedor = list(Seller.objects.filter(seller_id=seller_id).values())
        if len(vendedor) > 0:
            Seller.objects.filter(seller_id=seller_id).delete()
            datos = {'message': "datos actualizados"}
            return Response(json.dumps(datos),status=200)
        else: 
            datos = {'message': "Datos incorrectos"}
            return Response(status=400)