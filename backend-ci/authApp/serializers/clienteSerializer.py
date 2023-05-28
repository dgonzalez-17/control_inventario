from rest_framework import serializers    
from authApp.models.cliente import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Customer 
        fields = ['customer_id','name','lastName','documentType','documentNumber','mailAddress','phone','city','address','birthDate','nickName','password']

        def create(self, validated_data):
            clienteInstance = Customer.objects.create(**validated_data)
            return clienteInstance
        
        def to_representation(self, obj):
            user= Customer.objects.get(id=obj.id)
            return {
                'name': Customer.name,
                'lastName': Customer.lastName,
                'documentType': Customer.documentType,
                'documentNumber': Customer.documentNumber,
                'mailAddress': Customer.mailAddress,
                'phone': Customer.phone,
                'city': Customer.city,
                'address': Customer.address,
                'birthDate': Customer.birthDate,
                'nickName': Customer.nickName,
                'password': Customer.password
            }