from rest_framework import status, permissions, viewsets, views
from authApp.models.proveedor import Proveedor
from rest_framework.response import Response
from authApp.serializers.proveedorSerializer import ProveedorSerializer
import json 

class ProveedorDeleteView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProveedorSerializer

    def delete(self, request,proveedor_id,):
        proveedor = list(Proveedor.objects.filter(proveedor_id=proveedor_id).values())
        if len(proveedor) > 0:
            Proveedor.objects.filter(proveedor_id=proveedor_id).delete()
            datos = {'message': "proveedor eliminado"}
            return Response(json.dumps(datos),status=200)
        else: 
            datos = {'message': "Datos incorrectos"}
            return Response(status=400)
