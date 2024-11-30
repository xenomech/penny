from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from ..models import Transaction


# Create
class CreateTransactionView(LoginRequiredMixin, CreateView):
    login_url = "login"
    model = Transaction
    template_name = "transaction/create_or_update_transaction.html"
    fields = ["title", "description", "amount", "date", "transaction_type"]
    success_url = reverse_lazy("core:list_all_transactions")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# Read
class TransactionListView(LoginRequiredMixin, ListView):
    login_url = "login"
    template_name = "index.html"
    context_object_name = "transactions"
    model = Transaction

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


# Update
# class EditTransactionView(LoginRequiredMixin, UpdateView):
#     login_url = "login"
#     model = Transaction
#     fields = ["title", "description"]
#     template_name = "forms/edit_form.html"
#     success_url = reverse_lazy("core:list_all_transactions")

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.filter(user=self.request.user)


# Delete
# class DeleteTransactionView(LoginRequiredMixin, DeleteView):
#     login_url = "login"
#     model = Transaction
#     success_url = reverse_lazy("core:list_all_transactions")

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.filter(user=self.request.user)
