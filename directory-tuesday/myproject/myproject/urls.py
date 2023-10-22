from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('information/', views.ghazaview),
    path('home/', views.form_view),
    path('shoma/', views.formedo_view),
]
