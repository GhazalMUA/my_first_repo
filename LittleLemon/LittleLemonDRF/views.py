from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def RatingsView(request):
    context= "<html><body><h1>welcome</h1></body></html>"  
    return HttpResponse(context)


