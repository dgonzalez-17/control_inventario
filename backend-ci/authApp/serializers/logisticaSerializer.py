from rest_framework import serializers    
from authApp.models.logistica   import Logistic

class LogisticSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Logistic
        fields = ['Logistics_id','name','lastName','documentType','documentNumber','mailAddress','phone','city','address','birthDate','nickName','password']

        def create(self, validated_data):
            logisticInstance = Logistic.objects.create(**validated_data)
            return logisticInstance
        
        def to_representation(self, obj):
            user= Logistic.objects.get(id=obj.id)
            return {
                'name': Logistic.name,
                'lastName': Logistic.lastName,
                'documentType': Logistic.documentType,
                'documentNumber': Logistic.documentNumber,
                'mailAddress': Logistic.mailAddress,
                'phone': Logistic.phone,
                'city': Logistic.city,
                'address': Logistic.address,
                'birthDate': Logistic.birthDate,
                'nickName': Logistic.nickName,
                'password': Logistic.password
            }