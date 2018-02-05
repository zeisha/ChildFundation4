from django.urls import path
from .views import *
from django.conf.urls import url, include

urlpatterns = [
    path('', HamyarHomeView, name='hamyar-home'),
    path('goals/', HamyarGoalsView.as_view(), name='hamyar-goals'),
    path('contact/', HamyarContactView.as_view(), name='hamyar-contact'),
    path('history/', HamyarHistoryView.as_view(), name='hamyar-history'),
    path('chart/', HamyarChartView.as_view(), name='hamyar-chart'),
    path('ehda/', EhdaView, name='ehda'),
    path('ehda-receipt/', EhdaReceiptListView, name='ehda-receipt'),
    path('letters-box/', LettersBoxView, name='letters-box'),
    path('madadjoo-contact/', MadadjooContactView.as_view(), name='madadjoo-contact'),
    path('madadjoo-list/', MadadjooListView, name='madadjoo-list'),
    path('pay/', PayView, name='pay'),
    path('pay-receipt/', PayReceiptListView, name='pay-receipt-list'),
    path('search/', SearchView, name='search'),
    path('modir-message/', ModirMessageView, name='modir-message'),
    path('edit_profile/', edit_profile, name = 'edit_profile'),
    path('logout/', logout, name='hamyar-logout'),
    path('search_result/', SerchResultView, name='search-result'),
    path('pay-foundation/', PayFoundationView, name='pay-foundation'),
    path('message-detail/<int:pk>', message_detail, name='hamyar-message-detail'),
]
