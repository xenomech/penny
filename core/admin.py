from django.contrib import admin
from .models import BankAccount, Card, Transaction, Profile, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
admin.site.register(BankAccount)
admin.site.register(Card)
admin.site.register(Transaction)
admin.site.register(Profile)
admin.site.register(User, BaseUserAdmin)
