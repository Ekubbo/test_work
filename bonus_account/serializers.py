from rest_framework import serializers
from .models import Transaction, Account


class AccountSerializers(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'


class TransactionSerializers(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'


class CreateAccountSerializers(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ("first_name", "last_name", "phone", "cart_number")
