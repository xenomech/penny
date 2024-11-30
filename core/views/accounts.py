from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from ..models import BankAccount

from ..constants.providers import ACCOUNT_PROVIDERS_INDIA


class CreateOrUpdateBankAccountView(LoginRequiredMixin, CreateView):
    providers = ACCOUNT_PROVIDERS_INDIA
    login_url = "login"
    model = BankAccount
    fields = ["name", "provider", "balance"]
    template_name = "account/create_or_update_bank_account.html"
    success_url = reverse_lazy("core:list_all_bank_accounts")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["providers"] = self.providers
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ListAllBankAccountsView(LoginRequiredMixin, ListView):
    login_url = "login"
    model = BankAccount
    template_name = "account/list_all_bank_accounts.html"
    context_object_name = "bank_accounts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        headers = {
            "name": "Name",
            "provider": "Provider",
            "balance": "Balance",
        }
        
        values = [
            {
                "name": bank_account.name,
                "provider": bank_account.provider,
                "balance": bank_account.balance,
            }
            for bank_account in context["bank_accounts"]
        ]
        
        context.update({
            "headers": headers,
            "values": values,
        })
        
        return context
