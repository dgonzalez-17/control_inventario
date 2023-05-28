from rest_framework import status, permissions, viewsets, views
from authApp.models.vendedor import Seller
from rest_framework.response import Response
from authApp.serializers.vendedorSerializer import SellerSerializer
import json
from django.http.response import JsonResponse


class SellerUpdateView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SellerSerializer

    def put(self, request,seller_id,):
        jd = json.loads(request.body)
        vendedor = list(Seller.objects.filter(seller_id=seller_id).values())
        if len(vendedor) > 0:
            vend = Seller.objects.get(seller_id=seller_id)
            vend.sellerCode=jd['sellerCode']
            vend.name=jd['name']
            vend.lastName=jd['lastName']
            vend.documentType=jd['documentType']
            vend.documentNumber=jd['documentNumber']
            vend.mailAddress=jd['mailAddress']
            vend.phone=jd['phone']
            vend.city=jd['city']
            vend.address=jd['address']
            vend.birthDate=jd['birthDate']  
            vend.nickName=jd['nickName']
            vend.password=jd['password']
            vend.save()
            datos = {'message': "datos actualizados"}
            return Response(json.dumps(datos),status=200)
        else: 
            datos = {'message': "Datos incorrectos"}
            return Response(status=400)