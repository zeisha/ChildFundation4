from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', include('MySite.urls'), name='my-site'),
    path('admin/', admin.site.urls),
]
