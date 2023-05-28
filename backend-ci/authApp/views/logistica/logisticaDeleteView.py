from rest_framework import status, permissions, viewsets, views
from authApp.models.logistica import Logistic
from rest_framework.response import Response
from authApp.serializers.logisticaSerializer import LogisticSerializer
import json 

class LogisticDeleteView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LogisticSerializer

    def delete(self, request,Logistics_id,):
        proveedor = list(Logistic.objects.filter(Logistics_id =Logistics_id).values())
        if len(proveedor) > 0:
            Logistic.objects.filter(Logistics_id=Logistics_id).delete()
            datos = {'message': "logistica eliminado"}
            return Response(json.dumps(datos),status=200)
        else: 
            datos = {'message': "Datos incorrectos"}
            return Response(status=400)
