from django.conf.urls import url, include
from django.urls import path
from .views import *
from karbar.views import login

urlpatterns = [
    path('hamyar/', include('hamyar.urls'), name="hamyar"),
    path('madadju/', include('madadju.urls'), name='madadju'),
    path('madadkar/', include('madadkar.urls'), name='madadkar'),
    path('modir/', include('modir.urls'), name='modir'),
    path('', home, name='home'),
    path('chart/', chart, name='chart'),
    path('goals/', goals, name='goals'),
    path('history/', history, name='history'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('login/', login, name='login'),
    path('register/', RegisterView.as_view(), name='hamyar-register'),
    path('hamyar-profile/', include('hamyar.urls2'), name="hamyar-profile"),
    # TODO
    # path('madadju-search/', , name='madadju-search'),
]
