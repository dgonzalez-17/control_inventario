from rest_framework import serializers    
from authApp.models.proveedor import Proveedor

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Proveedor 
        fields = ['proveedor_id','name','lastName','documentType','documentNumber','mailAddress','phone','city','address','birthDate','nickName','password']

        def create(self, validated_data):
            proveedorInstance = Proveedor.objects.create(**validated_data)
            return proveedorInstance
        
        def to_representation(self, obj):
            user= Proveedor.objects.get(id=obj.id)
            return {
                'name': Proveedor.name,
                'lastName': Proveedor.lastName,
                'documentType': Proveedor.documentType,
                'documentNumber': Proveedor.documentNumber,
                'mailAddress': Proveedor.mailAddress,
                'phone': Proveedor.phone,
                'city': Proveedor.city,
                'address': Proveedor.address,
                'birthDate': Proveedor.birthDate,
                'nickName': Proveedor.nickName,
                'password': Proveedor.password
            }