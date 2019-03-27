from django.db import models
from django.core.validators import MinValueValidator


TRANSACTION_TYPE = (
    ("Pay.", "Payment", ),
    ("Bon.", "Bonus payment", ),
    ("Acc", "Bonus accrual", ),
)


class Account(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    cart_number = models.IntegerField(unique=True, validators=[MinValueValidator(1)])
    balance = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return "{} {}".format(self.last_name, self.first_name)


class Transaction(models.Model):
    transaction_type = models.CharField(max_length=20,
                                        choices=TRANSACTION_TYPE,
                                        default=TRANSACTION_TYPE[0][0])
    amount = models.IntegerField(validators=[MinValueValidator(1)])
    date = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        super(Transaction, self).save(*args, **kwargs)

        if self.transaction_type == TRANSACTION_TYPE[1][0]:
            self.account.balance = self.account.balance - self.amount
            self.account.save()
        elif self.transaction_type == TRANSACTION_TYPE[2][0]:
            self.account.balance = self.account.balance + self.amount
            self.account.save()
