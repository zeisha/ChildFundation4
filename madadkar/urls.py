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
    path('madadjulist/', madadkar.views.MadadjooListView, name='madadkar-list'),
    path('editneed/<username>', madadkar.views.editneed, name='editneed'),
    path('instantneed/<username>', madadkar.views.instantneed, name='instantneed'),
    path('madadju-register/', MadadkarMadadjuregister.as_view(), name='madadkar-madadju-register'),
    path('managesaving1/<username>', madadkar.views.managesaving1, name='managesaving1'),
    path('managesaving2/<username>', madadkar.views.managesaving2, name='managesaving2'),
    path('receipt/<username>', madadkar.views.receipt, name='receipt'),
    path('report/<username>', report, name='report'),
    path('seemsg/', madadkar.views.seemsg, name='seemsg'),
    path('seereq/', madadkar.views.seereq, name='seereq'),
    path('success/<username>', madadkar.views.success, name='success'),
    path('taaligh/<username>', madadkar.views.taaligh, name='taaligh'),
    path('logout/', logout, name='madadkar-logout'),
    path('showneed/<username>', needShow, name='showneed'),
    path('message-detail/<int:pk>', message_detail, name='madadkar-message-detail'),
    path('letters-box/', LettersBoxView, name='madadkar-letters-box'),
    path('search/', SearchView, name='madadkar-search'),
    path('search_result/', SerchResultView, name='madadkar-search-result'),

]
