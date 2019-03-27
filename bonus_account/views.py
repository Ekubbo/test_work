from .models import Account, Transaction
from .serializers import AccountSerializers, TransactionSerializers, CreateAccountSerializers
from rest_framework import generics


class ListAccountsView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializers


class AccountDetailsView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializers
    model = Account
    lookup_field = 'cart_number'


class ListTransactionsView(generics.ListAPIView):
    serializer_class = TransactionSerializers
    model = Transaction

    def get_queryset(self):
        cart_number = self.request.query_params.get('cart_number', None)

        if cart_number and cart_number.isnumeric():
            queryset = self.model.objects.filter(account__cart_number=cart_number)
            return queryset
        return []


class CreateAccountView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = CreateAccountSerializers
