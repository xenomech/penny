from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from ..models import Transaction


# Create
class CreateTransactionView(LoginRequiredMixin, CreateView):
    login_url = "login"
    model = Transaction
    template_name = "transaction/create_transaction.html"
    fields = ["title", "description", "amount", "date", "transaction_type"]
    success_url = reverse_lazy("core:transaction_index")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# Read
class TransactionListView(LoginRequiredMixin, ListView):
    login_url = "login"
    template_name = "transaction/list_transactions.html"
    context_object_name = "transactions"
    model = Transaction

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

class TransactionDetailView(LoginRequiredMixin, DetailView):
    login_url = "login"
    model = Transaction
    template_name = "transaction/show_transaction.html"
    context_object_name = "transaction"


class UpdateTransactionView(LoginRequiredMixin, UpdateView):
    login_url = "login"
    model = Transaction
    template_name = "transaction/update_transaction.html"
    fields = ["title", "description", "amount", "date", "transaction_type"]
    success_url = reverse_lazy("core:transaction_index")



class DeleteTransactionView(LoginRequiredMixin, DeleteView):
    login_url = "login"
    model = Transaction
    success_url = reverse_lazy("core:transaction_index")
