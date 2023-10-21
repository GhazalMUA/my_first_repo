from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('Home/' , views.form_view)
]