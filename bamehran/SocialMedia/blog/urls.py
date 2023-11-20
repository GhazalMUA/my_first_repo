from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home , name='home'),
    path( 'article/<slug:slug>' , views.detail , name='detail')
#The <slug:slug> part is a URL parameter capturing a slug and passing it to the detail view. So, when a user visits a URL like "/article/some-example-slug/", Django captures "some-example-slug" and passes it as the slug parameter to the detail view.
]