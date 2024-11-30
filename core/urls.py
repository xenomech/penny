from django.urls import path, include
from .views.transactions import TransactionListView
app_name = "core"
urlpatterns = [
    path("", TransactionListView.as_view(), name="list_all_transactions"),
]

urlpatterns += [
    path("accounts/", include("core.routes.accounts")),
    path("cards/", include("core.routes.cards")),
    path("transactions/", include("core.routes.transactions")),
]
