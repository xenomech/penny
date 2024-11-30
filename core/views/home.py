from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Transaction, BankAccount


@login_required(login_url="/auth/login/")
def home(request):
    transactions = Transaction.objects.for_user(user=request.user).order_by("-date")[:10]
    accounts = BankAccount.objects.for_user(user=request.user).order_by("name")
    total_balance = sum(account.balance for account in accounts)
    context = {
        "transactions": transactions,
        "accounts": accounts,
        "total_balance": total_balance,
    }
    return render(request, "home/index.html", context)
