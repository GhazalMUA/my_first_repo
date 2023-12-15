from rest_framework import serializers
from .models import RestaurantMenu , Dastebandi
from decimal import Decimal
'''
class RestaurantSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    title=serializers.CharField(max_length=200)
    price=serializers.DecimalField(max_digits=6, decimal_places=2)
    inventory=serializers.IntegerField()    
'''



class DastebandiSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dastebandi
        fields = ['id' , 'slug' , 'title']
 
     
     
     
class RestaurantSerializer(serializers.ModelSerializer):
    stock=serializers.IntegerField(source='inventory')
    price_after_tax=serializers.SerializerMethodField(method_name='calculate_tax')
    price_after_discount=serializers.SerializerMethodField(method_name='calculate_20_discount')
    dastebandi= DastebandiSerializer(read_only=True)
    dastebandi_id= serializers.IntegerField(write_only=True)
    class Meta:
        model=RestaurantMenu
        fields= [ 'title','price', 'stock', 'price_after_tax', 'price_after_discount','dastebandi','dastebandi_id']
    def calculate_tax(self, product:RestaurantMenu):
        return product.price * Decimal(1.1)
    def calculate_20_discount(self, product:RestaurantMenu):
        result= product.price * Decimal (0.8)
        return (result)
    