
# Models for the Guitar Learning Blog / Forum application.

# This file defines:
# - Subject (categories)
# - Profile (user role extension)
# - Post (main learning posts)
# - Reply (discussion responses)
# - Resource (external learning links)
# - Vote (upvoting system)

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# STATUS CHOICES (For Draft / Published posts)

STATUS = (
    (0, "Draft"),
    (1, "Published"),
)

# SKILL LEVEL CHOICES (Used for users and posts)

LEVEL_CHOICES = [
    ('beginner', 'Beginner'),
    ('intermediate', 'Intermediate'),
    ('advanced', 'Advanced'),
    ('teacher', 'Teacher'),
]

# SUBJECT MODEL
# Represents categories like:
# - Practice
# - Equipment
# - Song Learning
# - Music Theory


class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        """
        Automatically generate slug from name
        if it hasn't been provided.
        """
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        String representation shown in admin.
        """
        return self.name

# PROFILE MODEL

# Extends Django's built-in User model.
# Adds skill level / role without replacing User.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default='beginner'
    )

    def __str__(self):
        return self.user.username

# POST MODEL
# Main learning content in the forum.


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)

    # Used for SEO-friendly URLs
    slug = models.SlugField(max_length=200, unique=True)

    # Author of the post
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts"
    )

    # Category of post
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="posts",
        null=True,
        blank=True
    )

    content = models.TextField()

    # Minimum skill level required
    min_level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default='beginner'
    )

    created_on = models.DateTimeField(auto_now_add=True)

    # Draft / Published
    status = models.IntegerField(
        choices=STATUS,
        default=0
    )

    def save(self, *args, **kwargs):
        """
        Automatically generate slug from title
        if it hasn't been provided.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# REPLY MODEL
# Represents responses to posts (discussion system).


class Reply(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='replies'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    content = models.TextField()

    # Allows teachers to verify helpful replies
    is_verified = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply by {self.author}"

# RESOURCE MODEL
# External learning materials attached to a post.
# Example:
# - YouTube lesson
# - Article
# - PDF


class Resource(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='resources'
    )

    added_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    # External URL
    url = models.URLField()

    description = models.TextField(blank=True)

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# VOTE MODEL
# Scalable voting system.
# A user can vote on:
# - A Post
# - A Reply
#
# Only one of post or reply should be filled.

class Vote(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='votes'
    )

    reply = models.ForeignKey(
        Reply,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='votes'
    )

    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Prevents a user from voting twice
        unique_together = ('user', 'post', 'reply')

    def __str__(self):
        return f"Vote by {self.user}"
