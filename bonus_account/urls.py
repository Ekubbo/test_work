from django.urls import path
from .views import ListAccountsView, AccountDetailsView, ListTransactionsView, CreateAccountView


urlpatterns = [
    path(r'accounts/', ListAccountsView.as_view(), name='accounts'),
    path(r'account/create/', CreateAccountView.as_view(), name='create-account'),
    path(r'account/details/<int:cart_number>/', AccountDetailsView.as_view(), name='details-account'),
    path(r'transactions/', ListTransactionsView.as_view(), name='transactions'),
]
