from django.urls import path
from ..views.settings import settings_edit

urlpatterns = [
    path("", settings_edit, name="settings_edit"),
]
