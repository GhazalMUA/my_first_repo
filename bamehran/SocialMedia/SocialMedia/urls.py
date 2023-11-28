
from django.contrib import admin
from django.urls import path, include
from weblog.views import logout_view
#from django.contrib.auth import logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('weblog.urls')),
    path('logout/' , logout_view , name='logout'),
]




from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)