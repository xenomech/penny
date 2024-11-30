from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models import BaseModel
from core.constants.currencies import CURRENCY_CHOICES
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    pass

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        Profile.objects.get_or_create(user=self)

class Profile(BaseModel):
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    settings = models.OneToOneField('Settings', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.settings_id:
            self.settings = Settings.objects.create(user=self.user)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class BankAccount(BaseModel):
    name = models.CharField(
        max_length=100, null=False, blank=False, default="Untitled Bank Account"
    )
    provider = models.CharField(max_length=100, null=False, blank=False)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.name} - {self.balance}"


class Card(BaseModel):
    card_number_ends_with = models.IntegerField()
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.card_number_ends_with} - {self.bank_account.name}"


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
    date = models.DateTimeField()
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

class Settings(BaseModel):
    THEME_LIGHT = "LIGHT"
    THEME_DARK = "DARK"
    THEME_CHOICES = [
        (THEME_LIGHT, "Light"),
        (THEME_DARK, "Dark"),
    ]
    theme = models.CharField(max_length=10, choices=THEME_CHOICES, default=THEME_LIGHT)
    preferred_currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="USD")
    
    def __str__(self):
        return self.theme + " - " + self.preferred_currency
