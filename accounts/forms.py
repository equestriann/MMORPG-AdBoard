from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AccountCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'myfield'})
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'myfield'})
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'myfield'})
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'myfield'})
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
