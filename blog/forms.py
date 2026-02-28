# User and Registration Forms


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment, Resource, Profile


class RegisterForm(UserCreationForm):

    # Extends Django's built-in UserCreationForm to
    # include email and role fields

    email = forms.EmailField(required=True)
    role = forms.ChoiceField(
        choices=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
        ],
        required=True,
        label='Role/Skill Level'
    )

    class Meta:
        model = User
        # Fields to include in the registration form
        fields = ['username', 'email', 'password1', 'password2', 'role']


class PostForm(forms.ModelForm):
    # Form for creating/editing posts

    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'min_level', 'subject']


class CommentForm(forms.ModelForm):
    # Form for creating/editing comments (replies)
    resource_title = forms.CharField(
        max_length=200, required=False,
        label='Resource Title'
    )
    resource_url = forms.URLField(
        required=False, label='Resource URL'
    )
    resource_description = forms.CharField(
        widget=forms.Textarea, required=False,
        label='Resource Description'
    )

    class Meta:
        model = Comment
        fields = [
            'content',
            'resource_title',
            'resource_url',
            'resource_description'
        ]


class ResourceForm(forms.ModelForm):
    # Form for creating/editing resources

    class Meta:
        model = Resource
        fields = ['title', 'url', 'description']


class ProfileForm(forms.ModelForm):
    # Form for editing the Profile model's role and bio fields

    class Meta:
        model = Profile
        fields = ['role', 'bio']
