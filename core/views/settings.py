from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import Settings

@login_required(login_url="login")
def settings_edit(request):
    if request.method == "POST":
        data = request.POST
        settings = Settings.objects.get(user=request.user)
        settings.theme = data["theme"]
        settings.save()
        response = redirect("core:home_index")
        response.set_cookie("theme", settings.theme)
        return response
    return render(request, "settings/user_preferences.html")
