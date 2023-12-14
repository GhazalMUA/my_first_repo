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





@api_view()
def restaurantmenu_view(request):
    items=RestaurantMenu.objects.all()
    serialized_item= RestaurantSerializer(items, many=True)
    serialized_data=serialized_item.data
    return Response(serialized_data)



@api_view()
def single_item(request, id):
#    item=RestaurantMenu.objects.get(pk=id)
    item= get_object_or_404(RestaurantMenu, pk=id)
    serialized_item= RestaurantSerializer(item)
    serialized_data=serialized_item.data
    return Response(serialized_data)
