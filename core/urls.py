from django.urls import path
from .views import TransactionListView

app_name = "core"
urlpatterns = [
    path("", TransactionListView.as_view(), name="list_all_transactions"),  # read all todo
    # path("create/", CreateTransactionView.as_view(), name="create_transaction"),  # create todo
    # path(
    #     "edit/<int:pk>/", EditTransactionView.as_view(), name="edit_transaction"
    # ),  # update todo
    # path(
    #     "delete/<int:pk>/", DeleteTransactionView.as_view(), name="delete_transaction"
    # ),  # delete todo
]
