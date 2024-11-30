from django.urls import path
from ..views.cards import (
    ListAllCardsView,
    CreateCardView,
    CardDetailView,
    UpdateCardView,
    DeleteCardView,
)

urlpatterns = [
    path("", ListAllCardsView.as_view(), name="card_index"),
    path("create/", CreateCardView.as_view(), name="card_new"),
    path("<int:pk>/", CardDetailView.as_view(), name="card_show"),
    path("update/<int:pk>/", UpdateCardView.as_view(), name="card_edit"),
    path("delete/<int:pk>/", DeleteCardView.as_view(), name="card_destroy"),
]
