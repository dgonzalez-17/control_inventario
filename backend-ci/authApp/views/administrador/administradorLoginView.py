from rest_framework import status, permissions, viewsets, views
from authApp.models.administrador import Administrator
from rest_framework.response import Response
from authApp.serializers.administradorSerializer import AdministratorSerializer
import json 

class AdministratorLoginView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AdministratorSerializer

    def post(self, request, *args, **kwargs): 
        administrator = list(Administrator.objects.filter(nickName=request.data['nickName']).values())
        if len(administrator) > 0:
            for nick in administrator:
                if nick['password'] == request.data['password']:
                    datos = {'message':"datos validados"}
                    return Response(json.dumps(datos),status=200)
            datos = {'message': "Password incorrecto"}        
            return Response(json.dumps(datos),status=401)
        else:
            datos = {'message': "Usuario Incorrecto"}
            return Response(json.dumps(datos),status=401)