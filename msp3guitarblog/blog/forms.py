# User and Registration Forms


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment


class RegisterForm(UserCreationForm):

    # Extends Django's built-in UserCreationForm to
    # include email and role fields

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        # Fields to include in the registration form
        fields = ['username', 'email', 'password1', 'password2']


class PostForm(forms.ModelForm):
    # Form for creating/editing posts

    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'min_level', 'subject']


class CommentForm(forms.ModelForm):
    # Form for creating/editing comments (replies)

    class Meta:
        model = Comment
        fields = ['content']
