from django.urls import path
from .views import *

urlpatterns = [
    path('', HamyarHomeView, name='hamyar-home'),
    path('goals/', HamyarGoalsView.as_view(), name='hamyar-goals'),
    path('contact/', HamyarContactView.as_view(), name='hamyar-contact'),
    path('history/', HamyarHistoryView.as_view(), name='hamyar-history'),
    path('chart/', HamyarChartView.as_view(), name='hamyar-chart'),
    path('enseraf/', EnserafView.as_view(), name='enseraf'),
    path('entekhab/', EntekhabView.as_view(), name='entekhab'),
    path('ehda/', EhdaView.as_view(), name='ehda'),
    path('ehda-receipt/', EhdaReceiptView.as_view(), name='ehda-receipt'),
    path('letters-box/', LettersBoxView.as_view(), name='letters-box'),
    path('madadjoo-contact/', MadadjooContactView.as_view(), name='madadjoo-contact'),
    path('madadjoo-list/', MadadjooListView, name='madadjoo-list'),
    path('pay/', PayView.as_view(), name='pay'),
    path('pay-receipt/', PayReceiptView.as_view(), name='pay-receipt'),
    path('search/', SearchView, name='search'),
    path('send-message/', SendMessageView.as_view(), name='send-message'),
    path('edit_profile/', edit_profile, name = 'edit_profile'),
    path('logout/', logout, name='hamyar-logout'),
    path('search_result/', SerchResultView, name='search-result'),
]
