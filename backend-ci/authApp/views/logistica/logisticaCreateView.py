from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.logisticaSerializer import LogisticSerializer
from authApp.models.logistica import Logistic
import json 
class LogisticCreateView(views.APIView):
    def post(self, request,*args, **kwargs):
        serializer = LogisticSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            datos = {'message':"datos validados"}
            return Response(json.dumps(datos),status=200)
        else:
            datos = {'message':"Error en el envío de datos"}
            return Response(json.dumps(datos),status=400)
            