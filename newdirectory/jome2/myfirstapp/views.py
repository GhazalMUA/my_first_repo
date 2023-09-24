from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def say_hello(request):
    return HttpResponse("salam khoshkelaaa")
def classes(request):
    matn ="""<h1 style="color: #335C81;">bodycombat</h1> <p1 style="color: #00A896; font-family: \'Arial\', sans-serif; font-size: 27px; background-color:#ad9b9a ; font-weight: medium; text-decoration: upperline;">baraye sabtenam inja click konin</p1>, <h1 style="color: #0f1a20;">bodypump</h1>"""
    return HttpResponse (matn)
def homepage(request):
    return HttpResponse("welcome to Studio-B !")
def clock(request):
    vaghtiomade=datetime.today()
    return HttpResponse(vaghtiomade)
def menu(request):
    text="""<h1 style="color: #Ed5237; font-family: 'Arial', sans-serif; font-size: 24px; font-weight: bold; text-decoration: underline;">
        This is STUDIO-B again!
    </h1>"""
    return HttpResponse(text)

def mainmenu(request, class_name):
    items = {
       'bodycombat' :'mix marshal art','bodypump': 'heavy muscles', 'bodybalance': 'like yoga'
    }
    

    tozihat = items[class_name]

    return HttpResponse(f"<h2>{class_name}</h2>" + tozihat)