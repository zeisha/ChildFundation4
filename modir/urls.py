from django.urls import path

from .views import *

urlpatterns = [
    path('', AdminHomeView.as_view(), name='admin-home'),
    path('goals/', AdminGoalsView.as_view(), name='admin-goals'),
    path('history/', AdminHistoryView.as_view(), name='admin-history'),
    path('chart/', AdminChartView.as_view(), name='admin-chart'),
    path('contact/', AdminContactView.as_view(), name='admin-contact'),
    path('hamyar-register/', AdminHamyarRegisterView.as_view(), name='admin-hamyar-register'),
    path('madadkar-register/', AdminMadadkarRegisterView.as_view(), name='admin-madadkar-register'),
    path('logout/', logout, name='admin-logout'),
    path('user-delete/', delete_user, name='admin-delete'),
    path('payments/', PaymentView.as_view(), name='admin-payment'),
    path('payments-madadju/', PaymentMadadjuView.as_view(), name='admin-payment-madadju'),
]
