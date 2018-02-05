from django.urls import path
from .views import *

urlpatterns = [
    path('', Enserafview2, name = 'test'),
    path('<username>/', EnserafView, name='inline-madadju-enseraf'),
]
