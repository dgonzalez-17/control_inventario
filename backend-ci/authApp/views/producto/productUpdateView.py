from itertools import product
from rest_framework import status, permissions, viewsets, views
from authApp.models.product import Product
from rest_framework.response import Response
from authApp.serializers.productoSerializer import ProductSerializer
import json
from django.http.response import JsonResponse


class ProductUpdateView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

    def put(self, request,producto_id,):
        jd = json.loads(request.body)
        product = list(Product.objects.filter( producto_id = producto_id).values())
        if len(product) > 0:
            prod = Product.objects.get( producto_id = producto_id)
            prod.nameProduto=jd['nameProduto']
            prod.marca=jd['marca']
            prod.precio_unitario=jd['precio_unitario']
            prod.talla=jd['talla']
            prod.color=jd['color']
            prod.save()
            datos = {'message': "datos actualizados"}
            return Response(json.dumps(datos),status=200)
        else: 
            datos = {'message': "Datos incorrectos"}
            return Response(status=400)

