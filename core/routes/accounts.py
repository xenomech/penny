from django.urls import path
from ..views.accounts import ListAllBankAccountsView, CreateBankAccountView, BankAccountDetailView, UpdateBankAccountView, DeleteBankAccountView

urlpatterns = [
    path("", ListAllBankAccountsView.as_view(), name="account_index"),
    path("create/", CreateBankAccountView.as_view(), name="account_new"),
    path("<int:pk>/", BankAccountDetailView.as_view(), name="account_show"),
    path("update/<int:pk>/", UpdateBankAccountView.as_view(), name="account_edit"),
    path("delete/<int:pk>/", DeleteBankAccountView.as_view(), name="account_destroy"),
]
