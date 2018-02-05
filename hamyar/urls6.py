from django.urls import path
from .views import *

urlpatterns = [
    path('', Enserafview2, name = 'test'),
    path('<int:pk>/', message_detail, name='hamyar-message-detail'),
]
