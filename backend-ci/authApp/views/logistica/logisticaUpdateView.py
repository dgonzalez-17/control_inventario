from rest_framework import status, permissions, viewsets, views
from authApp.models.logistica import Logistic
from rest_framework.response import Response
from authApp.serializers.logisticaSerializer import LogisticSerializer
import json
from django.http.response import JsonResponse

from authApp.serializers.logisticaSerializer import LogisticSerializer

class LogisticUpdateView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LogisticSerializer

    def put(self, request,Logistics_id,):
        jd = json.loads(request.body)
        logistic = list(Logistic.objects.filter( Logistics_id= Logistics_id).values())
        if len(logistic) > 0:
            logi = Logistic.objects.get( Logistics_id= Logistics_id)
            logi.name=jd['name']
            logi.lastName=jd['lastName']
            logi.documentType=jd['documentType']
            logi.documentNumber=jd['documentNumber']
            logi.mailAddress=jd['mailAddress']
            logi.phone=jd['phone']
            logi.city=jd['city']
            logi.address=jd['address']
            logi.birthDate=jd['birthDate']  
            logi.nickName=jd['nickName']
            logi.password=jd['password']
            logi.save()
            datos = {'message': "datos actualizados"}
            return Response(json.dumps(datos),status=200)
        else: 
            datos = {'message': "Datos incorrectos"}
            return Response(status=400)

