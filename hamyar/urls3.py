from django.urls import path
from .views import *

urlpatterns = [
    path('<username>/', PayView, name='inline-madadju-pay'),
]