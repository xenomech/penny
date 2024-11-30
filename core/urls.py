from django.urls import path
from .views.transactions import TransactionListView, CreateTransactionView
from .views.accounts import CreateOrUpdateBankAccountView, ListAllBankAccountsView
app_name = "core"
urlpatterns = [
    path("", TransactionListView.as_view(), name="list_all_transactions"),  # read all todo
    path("create/", CreateTransactionView.as_view(), name="create_or_update_transaction"),  # create todo
    path("accounts/create/", CreateOrUpdateBankAccountView.as_view(), name="create_or_update_bank_account"),  # create todo
    path("accounts/", ListAllBankAccountsView.as_view(), name="list_all_bank_accounts"),  # read all bank accounts
    # path(
    #     "edit/<int:pk>/", EditTransactionView.as_view(), name="edit_transaction"
    # ),  # update todo
    # path(
    #     "delete/<int:pk>/", DeleteTransactionView.as_view(), name="delete_transaction"
    # ),  # delete todo
]
