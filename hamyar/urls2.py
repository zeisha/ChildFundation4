from django.urls import path
from .views import *

urlpatterns = [
    path('<username>/', ProfileView, name='inline-hamyar-profile'),
]