from rest_framework import status, permissions, viewsets, views
from authApp.models.cliente import Customer
from rest_framework.response import Response
from authApp.serializers.clienteSerializer import CustomerSerializer

class CustomerDetailView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs): 
        customer = Customer.objects.all()
        serializer = self.serializer_class(instance=customer,many=True)   
        return Response(serializer.data, status=status.HTTP_200_OK)
        

