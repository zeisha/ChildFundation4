from django.urls import path

from .views import *

urlpatterns = [
    path('', login_required(AdminHomeView.as_view()), name='admin-home'),
    path('goals/', login_required(AdminGoalsView.as_view()), name='admin-goals'),
    path('history/', login_required(AdminHistoryView.as_view()), name='admin-history'),
    path('chart/', login_required(AdminChartView.as_view()), name='admin-chart'),
    path('contact/', login_required(AdminContactView.as_view()), name='admin-contact'),
    path('hamyar-register/', login_required(AdminHamyarRegisterView.as_view()), name='admin-hamyar-register'),
    path('madadkar-register/', login_required(AdminMadadkarRegisterView.as_view()), name='admin-madadkar-register'),
    path('logout/', logout, name='admin-logout'),
    path('user-delete/', delete_user, name='admin-delete'),
    path('payments/', login_required(PaymentView.as_view()), name='admin-payment'),
    path('payments-madadju/', login_required(PaymentMadadjuView.as_view()), name='admin-payment-madadju'),
    path('edit-chooseuser', login_required(ChooseUserEditView.as_view()), name='admin-edit-chooseuser'),
    path('edit-user/<int:pk>', edit_profile, name='admin-edit'),
    path('search/', SearchView, name='modir-search'),
    path('search_result/', SerchResultView, name='modir-search-result'),
    path('madadjoo-list/', MadadjooListView, name='modir-madadjoo-list'),
    path('messages', login_required(MessagesView.as_view()), name='admin-messages'),
    path('message-detail/<int:pk>', message_detail, name='admin-message-detail'),
]
