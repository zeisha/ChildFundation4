from django.urls import path
from .views import *

urlpatterns = [
    path('<username>/', EhdaView, name='inline-madadju-ehda'),
]

