from rest_framework import status, permissions, viewsets, views
from authApp.models.administrador import Administrator
from rest_framework.response import Response
from authApp.serializers.administradorSerializer import AdministratorSerializer

class AdministratorDetailView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AdministratorSerializer

    def get(self, request, *args, **kwargs): 
        administrator = Administrator.objects.all()
        serializer = self.serializer_class(instance=administrator,many=True)   
        return Response(serializer.data, status=status.HTTP_200_OK)
        

