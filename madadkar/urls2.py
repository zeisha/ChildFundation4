from django.urls import path
from .views import *

urlpatterns = [
    path('<username>/', madadkarviewh, name='inline-madadkar-profile'),
]