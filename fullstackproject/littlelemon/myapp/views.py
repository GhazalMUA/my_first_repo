from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import JsonResponse 
from .models import MenuItem , Book , RestaurantMenu
from .forms import MenuForm
from django.forms.models import model_to_dict
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from .serializers import RestaurantSerializer
from django.shortcuts import get_object_or_404 
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage


def form_view(request):
    form = MenuForm()
    if request.method == 'POST':
        form= MenuForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            modify = MenuItem(
                item_name=cd['item_name'],
                category=cd['category'],
                description=cd['description'],
            )
            modify.save()
        return JsonResponse(
            {"message":"successful"}
        )
    return render (request, 'form.html' , {"form":form})  




@csrf_exempt
def books(request):
    if request.method == 'GET':
        books = Book.objects.all().values()
        print(books)
        return JsonResponse ({"books:" : list(books)}, content_type='application/json; charset=utf-8')
    

    elif request.method == 'POST':
        title = request.POST.get('title', '')
        author = request.POST.get('author', '')
        price = request.POST.get('price', '')

        try:
            book = Book.objects.create(
                title=title,
                author=author,
                price=price
            )
            return JsonResponse(model_to_dict(book), status=201)
        except IntegrityError:
            return JsonResponse({"message": "invalid input"}, status=400)

    return JsonResponse({"message": "Invalid method"}, status=405)





@api_view(['GET','POST'])
def restaurantmenu_view(request):
    if request.method == 'GET':
        items=RestaurantMenu.objects.select_related('dastebandi').all()
        dastebandi_name= request.query_params.get('dastebandi')
        to_price= request.query_params.get('to_price')
        search= request.query_params.get('search')
        ordering= request.query_params.get('ordering')
        perpage= request.query_params.get('perpage' , default=2)
        page= request.query_params.get('page' , default=1)
        if dastebandi_name:
            items=items.filter(dastebandi__title=dastebandi_name)
        if to_price:
            items= items.filter(price__lte=to_price)
            #to filter to search for an exact price you should write>>> items=items.filter(price=to_price)
            # lte is a conditional operator or field lookups and 'price__lte' means price is less than or equal to a value.
        if search:
            items= items.filter(title__startswith=search)
        if ordering:
            ordering_fields= ordering.split(",")
            items= items.order_by(*ordering_fields)
            
        paginator= Paginator(items, per_page=perpage)
        try:
            items = paginator.page(number=page)
        except:
            items = []        
        serialized_item= RestaurantSerializer(items, many=True)
        serialized_data=serialized_item.data
        return Response(serialized_data)
    if request.method == 'POST':
        serialized_item= RestaurantSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data , status.HTTP_201_CREATED)




@api_view(['GET','POST'])
def single_item(request, id):
#    item=RestaurantMenu.objects.get(pk=id)
    item= get_object_or_404(RestaurantMenu, pk=id)
    serialized_item= RestaurantSerializer(item)
    serialized_data=serialized_item.data
    return Response(serialized_data)
