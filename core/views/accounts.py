from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from ..models import BankAccount

from ..constants.providers import ACCOUNT_PROVIDERS_INDIA


class CreateBankAccountView(LoginRequiredMixin, CreateView):
    providers = ACCOUNT_PROVIDERS_INDIA
    login_url = "login"
    model = BankAccount
    fields = ["name", "provider", "balance"]
    template_name = "account/create_bank_account.html"
    success_url = reverse_lazy("core:account_index")

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
    template_name = "account/list_bank_accounts.html"
    context_object_name = "bank_accounts"

class BankAccountDetailView(LoginRequiredMixin, DetailView):
    login_url = "login"
    model = BankAccount
    template_name = "account/show_bank_account.html"
    context_object_name = "bank_account"


class UpdateBankAccountView(LoginRequiredMixin, UpdateView):
    login_url = "login"
    model = BankAccount
    template_name = "account/update_bank_account.html"
    fields = ["name", "provider", "balance"]
    success_url = reverse_lazy("core:account_index")



class DeleteBankAccountView(LoginRequiredMixin, DeleteView):
    login_url = "login"
    model = BankAccount
    success_url = reverse_lazy("core:account_index")
