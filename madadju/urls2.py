from django.urls import path
from .views import *

urlpatterns = [
    path('<username>/', madadjuviewh, name='madadju-hamyar-profile'),
]