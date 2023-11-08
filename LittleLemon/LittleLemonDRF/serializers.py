from rest_framework import serializers
from .models import MenuItem
from decimal import Decimal





class MenuItemSerializer(serializers.ModelSerializer):
    mojodi=serializers.IntegerField(source='inventory')
    priceaftertax= serializers.SerializerMethodField(method_name='calculate_tax')
    class Meta:
     model=MenuItem
     fields=['id' , 'title' , 'price' , 'mojodi' , 'priceaftertax'] 
    def calculate_tax(self , product:MenuItem):
        return product.price*Decimal(1.1)