from rest_framework import status, permissions, views
from authApp.models.administrador import Administrator
from rest_framework.response import Response
from authApp.serializers.administradorSerializer import AdministratorSerializer
import json 

class AdministratorDeleteView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AdministratorSerializer

    def delete(self, request,administrator_id,):
        administrator = list(Administrator.objects.filter(administrator_id=administrator_id).values())
        if len(administrator) > 0:
            Administrator.objects.filter(administrator_id=administrator_id).delete()
            datos = {'message': "datos actualizados"}
            return Response(json.dumps(datos),status=200)
        else: 
            datos = {'message': "Datos incorrectos"}
            return Response(status=400)
