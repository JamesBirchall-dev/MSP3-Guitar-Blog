# User and Registration Forms


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment, Resource, Profile, LEVEL_CHOICES
from django_summernote.widgets import SummernoteWidget


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
    content = forms.CharField(widget=forms.Textarea())
    slug = forms.CharField(required=False, widget=SummernoteWidget())
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


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())
    # Form for creating/editing comments (replies)
    resource_title = forms.CharField(
        max_length=200, required=False,
        label='Resource Title'
    )
    resource_url = forms.URLField(
        required=False, label='Resource URL'
    )

    def clean_resource_url(self):
        url = self.cleaned_data.get('resource_url')
        if url and not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        return url
    resource_description = forms.CharField(
        widget=forms.Textarea(), required=False,
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

    def clean_url(self):
        url = self.cleaned_data.get('url')
        if url and not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        return url

    class Meta:
        model = Resource
        fields = ['title', 'url', 'description']


class ProfileForm(forms.ModelForm):
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
