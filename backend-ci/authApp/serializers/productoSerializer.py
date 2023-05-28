from itertools import product
from rest_framework import serializers
from authApp.models.product import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        fields = ['producto_id','nameProduto','marca','precio_unitario','talla','color']

        def create(self, validated_data):
            productInstance = Product.objects.create(**validated_data)
            return productInstance
        
        def to_representation(self, obj):
            user= Product.objects.get(id=obj.id)
            return {
                'producto_id': Product.producto_id,   
                'nameProduto': Product.nameProduto,
                'marca': Product.marca,
                'precio_unitario': Product.precio_unitario,
                'talla': Product.talla,
                'color': Product.color
                
            }

