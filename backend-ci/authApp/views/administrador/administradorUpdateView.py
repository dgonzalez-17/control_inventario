from rest_framework import status, permissions, viewsets, views
from authApp.models.administrador import Administrator
from rest_framework.response import Response
from authApp.serializers.administradorSerializer import AdministratorSerializer
import json
from django.http.response import JsonResponse

class AdministratorUpdateView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AdministratorSerializer

    def put(self, request,administrator_id,):
        jd = json.loads(request.body)
        administrator = list(Administrator.objects.filter(administrator_id=administrator_id).values())
        if len(administrator) > 0:
            admin = Administrator.objects.get(administrator_id=administrator_id)
            admin.name=jd['name']
            admin.lastName=jd['lastName']
            admin.documentType=jd['documentType']
            admin.documentNumber=jd['documentNumber']
            admin.mailAddress=jd['mailAddress']
            admin.phone=jd['phone']
            admin.city=jd['city']
            admin.address=jd['address']
            admin.birthDate=jd['birthDate']  
            admin.nickName=jd['nickName']
            admin.password=jd['password']
            admin.save()
            datos = {'message': "datos actualizados"}
            return Response(json.dumps(datos),status=200)
        else: 
            datos = {'message': "Datos incorrectos"}
            return Response(status=400)

