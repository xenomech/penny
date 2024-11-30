from django.contrib import admin
from .models import BankAccount, Card, Transaction, Profile, User, Settings
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
admin.site.register(BankAccount)
admin.site.register(Card)
admin.site.register(Transaction)
admin.site.register(Settings)
admin.site.register(Profile)

@admin.register(User)
class ExtendedUserAdmin(BaseUserAdmin):
    pass