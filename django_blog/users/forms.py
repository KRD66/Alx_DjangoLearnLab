from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Use default User if not using CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser  # Use User if not using CustomUser
        fields = ["username", "email", "password1", "password2"]
