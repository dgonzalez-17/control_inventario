from rest_framework import serializers    
from authApp.models.administrador import Administrator

class AdministratorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Administrator 
        fields = ['administrator_id','name','lastName','documentType','documentNumber','mailAddress','phone','city','address','birthDate','nickName','password']

        def create(self, validated_data):
            administradorInstance = Administrator.objects.create(**validated_data)
            return administradorInstance
        
        def to_representation(self, obj):
            user = Administrator.objects.get(id=obj.id)
            return {
                'name': Administrator.name,
                'nickName': Administrator.nickName,
                'password': Administrator.password
            }