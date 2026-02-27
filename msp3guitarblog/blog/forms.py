# User and Registration Forms


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):

    # Extends Django's built-in UserCreationForm to
    # include email and role fields

    email = forms.EmailFeld(required=True)

    class Meta:
        model = User
        # Fields to include in the registration form
        fields = ['username', 'email', 'password1', 'password2']
