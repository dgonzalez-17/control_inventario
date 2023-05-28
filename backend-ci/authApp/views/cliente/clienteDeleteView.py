from rest_framework import status, permissions, viewsets, views
from authApp.models.cliente import Customer
from rest_framework.response import Response
from authApp.serializers.clienteSerializer import CustomerSerializer
import json 

class CustomerDeleteView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomerSerializer

    def delete(self, request,customer_id,):
        customer = list(Customer.objects.filter(customer_id=customer_id).values())
        if len(customer) > 0:
            Customer.objects.filter(customer_id=customer_id).delete()
            datos = {'message': "cliente eliminado"}
            return Response(json.dumps(datos),status=200)
        else: 
            datos = {'message': "Datos incorrectos"}
            return Response(status=400)
