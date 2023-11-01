from django.urls import path
from LittleLemonDRF import views

urlpatterns = [
    path('ratings', views.RatingsView),
]
 
