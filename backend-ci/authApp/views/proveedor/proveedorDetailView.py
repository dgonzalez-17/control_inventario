from rest_framework import status, permissions, viewsets, views
from authApp.models.proveedor import Proveedor
from rest_framework.response import Response
from authApp.serializers.proveedorSerializer import ProveedorSerializer

class ProveedorDetailView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProveedorSerializer

    def get(self, request, *args, **kwargs): 
        proveedor = Proveedor.objects.all()
        serializer = self.serializer_class(instance=proveedor,many=True)   
        return Response(serializer.data, status=status.HTTP_200_OK)
        
