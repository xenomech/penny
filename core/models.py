from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models import BaseModel

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    pass


class Profile(BaseModel):
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class BankAccount(BaseModel):
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return (
            self.user.first_name + " " + self.user.last_name + " " + str(self.balance)
        )


class Card(BaseModel):
    card_number_ends_with = models.IntegerField()
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)

    def __str__(self):
        return (
            self.user.first_name
            + " "
            + self.user.last_name
            + " "
            + self.card_number_ends_with
        )


class Transaction(BaseModel):
    TRANSACTION_TYPE_INCOME = "INCOME"
    TRANSACTION_TYPE_EXPENSE = "EXPENSE"
    TRANSACTION_TYPE_CHOICES = [
        (TRANSACTION_TYPE_INCOME, "Income"),
        (TRANSACTION_TYPE_EXPENSE, "Expense"),
    ]
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPE_CHOICES,
        default=TRANSACTION_TYPE_EXPENSE,
    )
    from_account = models.ForeignKey(
        BankAccount, on_delete=models.CASCADE, related_name="from_account", null=False
    )
    from_card = models.ForeignKey(
        Card, on_delete=models.CASCADE, related_name="from_card", null=True
    )

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " " + str(self.amount)
