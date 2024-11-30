from django.urls import path, include
from .views.transactions import TransactionListView

app_name = "core"

urlpatterns = [
    path("", include("core.routes.home")),
    path("accounts/", include("core.routes.accounts")),
    path("cards/", include("core.routes.cards")),
    path("transactions/", include("core.routes.transactions")),
    path("settings/", include("core.routes.settings")),
]
