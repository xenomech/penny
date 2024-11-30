from django.urls import path
from ..views.transactions import TransactionListView, CreateTransactionView, TransactionDetailView, UpdateTransactionView, DeleteTransactionView

urlpatterns = [
    path("", TransactionListView.as_view(), name="transaction_index"),
    path("create/", CreateTransactionView.as_view(), name="transaction_new"),
    path("<int:pk>/", TransactionDetailView.as_view(), name="transaction_show"),
    path("update/<int:pk>/", UpdateTransactionView.as_view(), name="transaction_edit"),
    path("delete/<int:pk>/", DeleteTransactionView.as_view(), name="transaction_destroy"),
]
