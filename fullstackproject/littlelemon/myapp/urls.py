from django.urls import path
from . import views
urlpatterns = [
    path('form/' ,views.form_view , name='form' ),
    path('books/' , views.books),
    path('restaurant/' ,views.restaurantmenu_view),
    path('restaurant/<int:id>' , views.single_item)
]
