from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from myapp.forms import ghaz

def form_view(request):
    form = ghaz()
    context = {"form" : form}
    return render (request, "home.html",context)