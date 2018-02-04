from django.urls import path
from .views import *
import madadkar.views

urlpatterns = [
    path('', madadkar.views.madadkarhome, name='madadkar-home'),
    path('goals/', madadkar.views.madadkargoal, name='madadkar-goals'),
    path('history/', madadkar.views.madadkarhistory, name='madadkar-history'),
    path('chart/', madadkar.views.madadkarchart, name='madadkar-chart'),
    path('contact/', MadadkarContact.as_view(), name='madadkar-contact'),
    path('profile/', madadkar.views.madadkarprofile, name='madadkar-profile'),
    path('editmadadju/', madadkar.views.editmadadju, name='madadkar-edit-madadju'),
    path('editneed/', madadkar.views.editneed, name='editneed'),
    path('instantneed/', madadkar.views.instantneed, name='instantneed'),
    path('madadju-register/', madadkar.views.madadjuregister, name='madadkar-madadju-register'),
    path('managesaving/', madadkar.views.managesaving, name='managesaving'),
    path('receipt/', madadkar.views.receipt, name='receipt'),
    path('report/', Report.as_view(), name='report'),
    path('seemsg/', madadkar.views.seemsg, name='seemsg'),
    path('seereq/', madadkar.views.seereq, name='seereq'),
    path('success/', madadkar.views.success, name='success'),
    path('taaligh/', madadkar.views.taaligh, name='taaligh'),
    path('logout/', logout, name='madadkar-logout'),
]
