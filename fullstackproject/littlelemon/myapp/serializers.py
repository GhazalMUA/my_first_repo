from rest_framework import serializers
#from .models import RestaurantMenu

class RestaurantSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    title=serializers.CharField(max_length=200)
    price=serializers.DecimalField(max_digits=6, decimal_places=2)
    inventory=serializers.IntegerField()    
 #   ghazalooo=serializers.CharField(max_length=50)
#    class Meta:
 #       model=RestaurantMenu
#        fields= '__all__'