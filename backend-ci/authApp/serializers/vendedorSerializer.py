from rest_framework import serializers    
from authApp.models.vendedor import Seller

class SellerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Seller
        fields = ['seller_id','sellerCode','name','lastName','documentType','documentNumber','mailAddress','phone','city','address','birthDate','nickName','password']

        def create(self, validated_data):
            vendedorInstance = Seller.objects.create(**validated_data)
            return vendedorInstance
        
        def to_representation(self, obj):
            user= Seller.objects.get(id=obj.id)
            return {
                'sellerCode': Seller.sellerCode,   
                'name': Seller.name,
                'lastName': Seller.lastName,
                'documentType': Seller.documentType,
                'documentNumber': Seller.documentNumber,
                'mailAddress': Seller.mailAddress,
                'phone': Seller.phone,
                'city': Seller.city,
                'address': Seller.address,
                'birthDate': Seller.birthDate,
                'nickName': Seller.nickName,
                'password': Seller.password
            }
