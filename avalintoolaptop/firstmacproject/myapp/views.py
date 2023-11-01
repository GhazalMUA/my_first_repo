from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def salam(request):
    return HttpResponse("man az inja behet salam mikonam")
def safeye_pardakht(request):
    return HttpResponse('inja bayad pardakht koni')
