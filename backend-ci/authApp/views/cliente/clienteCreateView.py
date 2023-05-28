from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.clienteSerializer import CustomerSerializer
from authApp.models.cliente import Customer
import json
"""
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
"""
class CustomerCreateView(views.APIView):
    def post(self, request,*args, **kwargs):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            datos = {'message':"datos validados"}
            return Response(json.dumps(datos),status=200)
            #return Response(status.HTTP_201_CREATED)
        else:
            datos = {'message':"Error en el envío de datos"}
            return Response(json.dumps(datos),status=400)
            