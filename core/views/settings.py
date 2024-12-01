from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import Settings
from core.constants.themes import THEME_CHOICES

@login_required(login_url="login")
def settings_edit(request):
    context = {
        "theme_choices": THEME_CHOICES,
    }
    if request.method == "POST":
        data = request.POST
        settings = Settings.objects.get(user=request.user)
        settings.theme = data["theme"]
        settings.save()
        response = redirect("core:settings_edit")
        response.set_cookie("theme", settings.theme)
        return response
    return render(request, "settings/user_preferences.html", context)
