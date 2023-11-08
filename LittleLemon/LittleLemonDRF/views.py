
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer

@api_view(['POST' , 'GET'])
def books(request):
    return Response('LIST OF BOOKS', status=status.HTTP_200_OK)

@api_view(['GET' , 'POST'])
def menu_items(request):
    if request.method == 'GET':
        items= MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        return Response(serializer.data)
     