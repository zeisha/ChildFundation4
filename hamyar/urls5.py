from django.urls import path
from .views import *

urlpatterns = [
    path('', HamyarHomeView, name = 'test'),
    # path('<username>/', EnserafView, name='inline-madadju-enseraf'),
    # path('<username>/', HamyarHomeView, name='inline-madadju-dard'),
]
