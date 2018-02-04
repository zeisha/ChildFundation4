from madadju.views import *
from django.urls import path

urlpatterns = [
    path('<username>/', madadjuviewh, name='madadju-hamyar-view'),
]