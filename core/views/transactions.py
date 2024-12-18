from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from ..models import Transaction


# Create
class CreateTransactionView(LoginRequiredMixin, CreateView):
    login_url = "login"
    model = Transaction
    template_name = "transaction/create_transaction.html"
    fields = ["title", "description", "amount", "date", "transaction_type", "from_account"]
    optional_fields = ["from_card"]
    success_url = reverse_lazy("core:transaction_index")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Create Transaction"
        return context

    def get_form_class(self):
        form_class = super().get_form_class()
        for field in form_class.base_fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        return form_class
    
    # Update the bank account balance -- TODO: Isolate this logic to a service for less choke points
    def form_valid(self, form):
        form.instance.user = self.request.user
        bank_account = form.cleaned_data.get('from_account')
        if form.cleaned_data.get('transaction_type') == "INCOME":
            bank_account.balance += form.cleaned_data.get('amount')
        else:
            bank_account.balance -= form.cleaned_data.get('amount')
        bank_account.save() 
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
    template_name = "transaction/create_transaction.html"
    fields = ["title", "description", "amount", "date", "transaction_type", "from_account"]
    success_url = reverse_lazy("core:transaction_index")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Update Transaction"
        return context

    def get_initial(self):
        initial = super().get_initial()
        transaction = self.get_object()
        initial['title'] = transaction.title
        initial['description'] = transaction.description
        initial['amount'] = transaction.amount
        initial['date'] = transaction.date
        initial['transaction_type'] = transaction.transaction_type
        initial['from_account'] = transaction.from_account
        return initial
    
    # Update the bank account balance -- TODO: Isolate this logic to a service for less choke points
    def form_valid(self, form):
        form.instance.user = self.request.user
        bank_account = form.cleaned_data.get('from_account')
        if form.cleaned_data.get('transaction_type') == "INCOME":
            bank_account.balance += form.cleaned_data.get('amount')
        else:
            bank_account.balance -= form.cleaned_data.get('amount')
        bank_account.save() 
        return super().form_valid(form)



class DeleteTransactionView(LoginRequiredMixin, DeleteView):
    login_url = "login"
    model = Transaction
    success_url = reverse_lazy("core:transaction_index")
