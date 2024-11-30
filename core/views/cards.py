from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from ..models import Card
from django.contrib.auth.mixins import LoginRequiredMixin


class ListAllCardsView(LoginRequiredMixin, ListView):
    login_url = "login"
    model = Card
    template_name = "card/list_cards.html"
    context_object_name = "cards"


class CreateCardView(LoginRequiredMixin, CreateView):
    login_url = "login"
    model = Card
    template_name = "card/create_card.html"
    fields = ["card_number_ends_with", "bank_account"]
    success_url = reverse_lazy("core:card_index")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CardDetailView(LoginRequiredMixin, DetailView):
    login_url = "login"
    model = Card
    template_name = "card/show_card.html"
    context_object_name = "card"


class UpdateCardView(LoginRequiredMixin, UpdateView):
    login_url = "login"
    model = Card
    template_name = "card/update_card.html"
    fields = ["name", "number", "expiration_date", "cvv", "bank_account"]
    success_url = reverse_lazy("core:card_index")


class DeleteCardView(LoginRequiredMixin, DeleteView):
    login_url = "login"
    model = Card
    success_url = reverse_lazy("core:card_index")
