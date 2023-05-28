from itertools import product
from rest_framework import status, permissions, viewsets, views
from authApp.models.product import Product
from rest_framework.response import Response
from authApp.serializers.productoSerializer import ProductSerializer
import json 

class ProductDeleteView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

    def delete(self, request,producto_id,):
        product = list(Product.objects.filter(producto_id =producto_id).values())
        if len(product) > 0:
            Product.objects.filter(producto_id=producto_id).delete()
            datos = {'message': "datos actualizados"}
            return Response(json.dumps(datos),status=200)
        else: 
            datos = {'message': "Datos incorrectos"}
            return Response(status=400)
