from rest_framework import status, permissions, viewsets, views
from authApp.models.proveedor import Proveedor
from rest_framework.response import Response
from authApp.serializers.proveedorSerializer import ProveedorSerializer
import json
from django.http.response import JsonResponse

from authApp.serializers.proveedorSerializer import ProveedorSerializer

class ProveedorUpdateView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProveedorSerializer

    def put(self, request,proveedor_id,):
        jd = json.loads(request.body)
        proveedor = list(Proveedor.objects.filter(proveedor_id=proveedor_id).values())
        if len(proveedor) > 0:
            prov = Proveedor.objects.get(proveedor_id=proveedor_id)
            prov.name=jd['name']
            prov.lastName=jd['lastName']
            prov.documentType=jd['documentType']
            prov.documentNumber=jd['documentNumber']
            prov.mailAddress=jd['mailAddress']
            prov.phone=jd['phone']
            prov.city=jd['city']
            prov.address=jd['address']
            prov.birthDate=jd['birthDate']  
            prov.nickName=jd['nickName']
            prov.password=jd['password']
            prov.save()
            datos = {'message': "datos actualizados"}
            return Response(json.dumps(datos),status=200)
        else: 
            datos = {'message': "Datos incorrectos"}
            return Response(status=400)

