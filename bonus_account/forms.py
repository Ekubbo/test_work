from .models import Transaction, TRANSACTION_TYPE
from django import forms


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = [id, ]

    def clean(self):

        transaction_type = self.cleaned_data.get('transaction_type')

        if transaction_type == TRANSACTION_TYPE[1][0]:
            account = self.cleaned_data.get('account')
            amount = self.cleaned_data.get('amount')

            if amount and account.balance < amount:
                self.add_error('account', "Not enough bonus account.")

        return self.cleaned_data
