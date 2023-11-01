"""
URL configuration for jome2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myfirstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('say_hello/', views.say_hello ),
    path('classes/' , views.classes),
    path('homepage', views.homepage),
    path('clock/', views.clock),
    path('menu/', views.menu),
    path('kelasha/<str:class_name>' , views.mainmenu),
]
