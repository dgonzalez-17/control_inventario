from rest_framework import status, permissions, viewsets, views
from authApp.models.cliente import Customer
from rest_framework.response import Response
from authApp.serializers.clienteSerializer import CustomerSerializer
import json
from django.http.response import JsonResponse

class CustomerUpdateView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomerSerializer

    def put(self, request,customer_id,):
        jd = json.loads(request.body)
        customer = list(Customer.objects.filter(customer_id=customer_id).values())
        if len(customer) > 0:
            custom = Customer.objects.get(customer_id=customer_id)
            custom.name=jd['name']
            custom.lastName=jd['lastName']
            custom.documentType=jd['documentType']
            custom.documentNumber=jd['documentNumber']
            custom.mailAddress=jd['mailAddress']
            custom.phone=jd['phone']
            custom.city=jd['city']
            custom.address=jd['address']
            custom.birthDate=jd['birthDate']  
            custom.nickName=jd['nickName']
            custom.password=jd['password']
            custom.save()
            datos = {'message': "datos actualizados"}
            return Response(json.dumps(datos),status=200)
        else: 
            datos = {'message': "Datos incorrectos"}
            return Response(status=400)

