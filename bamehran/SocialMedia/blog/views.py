from django.shortcuts import render , get_object_or_404
from .models import Article
# Create your views here.
def home(request):
    context={
        "articles": Article.objects.filter(status='p').order_by('-publish')
    }
    return render(request , 'blog/home.html' ,context )

def detail(request , slug):
    #In this line, slug is a parameter of the detail function. When you define a view function in Django, it often takes parameters that represent information extracted from the URL. In this case, slug is likely to be part of the URL for this view.
    context={
         "article" : get_object_or_404(Article , slug=slug)
#ghbln in bod bjay balai__>  "article" : Article.objects.get(slug=slug)
    }
    return render(request , 'blog/detail.html' , context)