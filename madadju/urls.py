from django.conf.urls import url, include
from django.urls import path
from .views import *
import madadju.views

urlpatterns = [
    path('', madadju.views.madadjuhome, name='madadju-home'),
    path('goals/', madadju.views.madadjugoal, name='madadju-goals'),
    path('history/', madadju.views.madadjuhistory, name='madadju-history'),
    path('chart/', madadju.views.madadjuchart, name='madadju-chart'),
    path('contact/', MadadjuContact.as_view(), name='madadju-contact'),
    path('madadkar-change/', madadju.views.madadkarchange, name='madadju-madadkar-change'),
    path('profile/', madadju.views.madadjuprofile, name='madadju-profile'),
    path('sendmsg/', MadadjuMsg.as_view(), name='madadju-msg'),
]
