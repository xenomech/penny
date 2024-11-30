from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

widget_attrs = {
    # "class": "form-control bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
}


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={**widget_attrs, "placeholder": "Username or Email"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={**widget_attrs, "placeholder": "Password"})
    )



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={**widget_attrs, "placeholder": "Email"}),
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={**widget_attrs, "placeholder": "Username"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={**widget_attrs, "placeholder": "Password"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={**widget_attrs, "placeholder": "Confirm Password"}
        )
    )

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password1", "password2"]
