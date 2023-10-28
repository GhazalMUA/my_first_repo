from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import Logform , ghaza , userform
# Create your views here.

from myapp.forms import ghaz

def form_view(request):
    form = userform()
    if request.method == 'POST' :
        form =userform(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render (request, "home.html",context)



def formedo_view(request):
    form = Logform()
    if request.method == 'POST' :
        form =Logform(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}     
    return render(request, "link.html" , context)   



def ghazaview(request):
    form = ghaza()
    if request.method == 'POST' :
        form= ghaza(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form} 
    return render (request , "ht2.html" , context)        




def about(request):
    about_mohtava = {'about' : "inja site e ghazal mua st. dige base fekonm dood maghzeto baste"}
    return render(request, 'about.html' , about_mohtava)


