"""
Forms used for user input in the application.

Includes forms for:
- User registration
- Post creation
- Comment submission
- Resource submission
- Profile editing
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment, Resource, Profile, LEVEL_CHOICES
from django_summernote.widgets import SummernoteWidget


class RegisterForm(UserCreationForm):
    """
    Extends Django's UserCreationForm to include:

    - Email field (required)
    - Role/Skill Level selection
      Options: beginner, intermediate, advanced

    This form is used for registering new users with
    additional metadata stored in Profile.
    """
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

# -----------------------------------------------------
# POST FORM
# -----------------------------------------------------


class PostForm(forms.ModelForm):
    """
    Form used for creating or editing learning posts.

    Features:
    - `content` rendered with Summernote rich text editor
    - `slug` optional for custom URL slug
    - `min_level` to indicate the minimum skill level required
    - `subject` defaults to 'Uncategorized' if new post
    - `tags` selectable via checkbox widget
    """
    content = forms.CharField(widget=SummernoteWidget())
    slug = forms.SlugField(required=False)
    min_level = forms.ChoiceField(choices=LEVEL_CHOICES, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set default subject to 'Uncategorized' if creating a new post
        if not self.instance.pk:
            try:
                from .models import Subject
                uncategorized = Subject.objects.get(slug="uncategorized")
                self.fields['subject'].initial = uncategorized.pk
            except Subject.DoesNotExist:
                pass

    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'min_level', 'subject', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
# -----------------------------------------------------
# COMMENT FORM
# -----------------------------------------------------


class CommentForm(forms.ModelForm):
    """
    Form for creating or editing comments.

    Supports optional creation of a resource when submitting a comment.
    Fields:
    - content: comment text (rich text)
    - resource_title, resource_url,
    resource_description: optional resource info
    """
    content = forms.CharField(widget=SummernoteWidget())
    # Optional Form for creating/editing comments (replies)
    resource_title = forms.CharField(
        max_length=200, required=False,
        label='Resource Title'
    )
    resource_url = forms.URLField(
        required=False, label='Resource URL'
    )
    resource_description = forms.CharField(
        widget=SummernoteWidget(), required=False,
        label='Resource Description'
    )

    def clean_resource_url(self):
        url = self.cleaned_data.get('resource_url')
        if url and not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        return url

    class Meta:
        model = Comment
        fields = [
            'content',
            'resource_title',
            'resource_url',
            'resource_description'
        ]


class ResourceForm(forms.ModelForm):
    """
    Ensure the URL starts with http:// or https://.
    Adds https:// by default if missing.
    """
    description = forms.CharField(widget=SummernoteWidget())

    def clean_url(self):
        url = self.cleaned_data.get('url')
        if url and not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        return url

    class Meta:
        model = Resource
        fields = ['title', 'url', 'description']


class ProfileForm(forms.ModelForm):
    """
    Form for editing user profile.

    Fields:
    - role (skill level, excluding 'teacher' to prevent accidental role change)
    - bio (rich text with Summernote)
    """
    bio = forms.CharField(widget=SummernoteWidget(), required=False)
    # Form for editing the Profile model's role and bio fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # exclude teacher from edit profile form
        self.fields['role'].choices = [
            (value, label) for value, label in self.fields['role'].choices
            if value != 'teacher'
        ]

    class Meta:
        model = Profile
        fields = ['role', 'bio']
