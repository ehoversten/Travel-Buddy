from django import forms

from .models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "username", "passwd"]
        help_texts = {
        "name": None,
        'username': None,
        'password': None,
    }

