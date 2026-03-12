"""
Models for the Guitar Learning Blog / Forum application.

This file defines the core database structure:

- Subject (content categories)
- Tag (topic labels)
- Profile (extends the Django User model)
- Post (main learning content)
- Comment (discussion responses)
- Resource (external learning materials)
- Like (voting system)

Relationships:
Users → create Posts, Comments, and Resources.
Posts → belong to Subjects and may have Tags.
Resources → may be attached to Posts or Comments.
Likes
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver

# -----------------------------------------------------
# CONSTANTS
# -----------------------------------------------------

# Post publishing status

STATUS = (
    (0, "Draft"),
    (1, "Published"),
)

# Skill levels used for users and post difficulty

LEVEL_CHOICES = [
    ('beginner', 'Beginner'),
    ('intermediate', 'Intermediate'),
    ('advanced', 'Advanced'),
    ('teacher', 'Teacher'),
]

# -----------------------------------------------------
# SUBJECT MODEL
# -----------------------------------------------------


class Subject(models.Model):
    """
    Represents a category of guitar learning content.

    Example subjects:
    - Practice
    - Music Theory
    - Equipment
    - Song Learning
    """

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    short_description = models.TextField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    # short description for listing pages
    short_description = models.TextField(max_length=255, blank=True, null=True)

    tags = models.ManyToManyField(
        'Tag',
        related_name='subjects',
        blank=True
    )

    def save(self, *args, **kwargs):
        # Automatically generate slug from name if not provided.
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        # String representation shown in admin.
        return self.name


# -----------------------------------------------------
# TAG MODEL
# -----------------------------------------------------
    """
    Tags are used to label posts with specific topics.

    Example:
    - Chords
    - Fingerstyle
    - Improvisation
    """


class Tag(models.Model):
    # Tags are used to label posts with specific topics.
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# -----------------------------------------------------
# PROFILE MODEL
# -----------------------------------------------------


class Profile(models.Model):

    """
    Extends Django's default User model.

    Stores:
    - user role / skill level
    - biography
    - reputation statistics
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    role = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default='beginner'
    )

    bio = models.TextField(
        blank=True,
        null=True
    )

    # -------------------------------------------------
    # Reputation properties
    # -------------------------------------------------

    @property
    def total_likes_received(self):
        """
        Calculates the total number of likes received
        across the user's posts, comments and resources.
        """
        post_likes = sum(
            post.likes.count() for post in self.user.blog_posts.all()
        )
        comment_likes = sum(
            comment.likes.count()
            for comment in self.user.comment_set.all()
        )
        resource_likes = sum(
            resource.likes.count()
            for resource in self.user.resources.all()
        )
        return post_likes + comment_likes + resource_likes

    @property
    def total_likes_cast(self):
        """
        Total number of likes the user has given to others.
        """
        return self.user.like_set.count()

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# -----------------------------------------------------
# POST MODEL
# -----------------------------------------------------


class Post(models.Model):
    """
    Main learning content created by teachers.

    Posts belong to a Subject and can include Tags.
    """
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
        related_name="posts"
    )

    # tags for filtering
    tags = models.ManyToManyField(
        Tag,
        related_name='posts',
        blank=True
    )

    content = models.TextField()
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
        Automatically generate slug from title.
        """

        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def like_count(self):
        return self.likes.count()

    def __str__(self):
        return self.title

# -----------------------------------------------------
# RESOURCE MODEL
# -----------------------------------------------------


class Resource(models.Model):
    """
    External learning materials attached to a post.

    Example resources:
    - YouTube lesson
    - Article
    - PDF
    """

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="resources",
        null=True,
        blank=True
    )
    # A resource can be attached to either a post or a comment (reply).
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='resources',
        null=True,
        blank=True
    )
    # A resource can also be attached to a comment (reply)
    comment = models.ForeignKey(
        'Comment',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='resources'
    )
    # The user who added the resource (for attribution and voting)
    added_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="resources"
    )

    title = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField(blank=True)
    verified = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        Automatically assign subject from post or comment if not set.
        This ensures resources are categorized even if the user
        doesn't select a subject.
        """
        if self.post:
            self.subject = self.post.subject

        elif self.comment:
            self.subject = self.comment.post.subject

        super().save(*args, **kwargs)

    @property
    def like_count(self):
        return self.likes.count()

    def __str__(self):
        return self.title

# -----------------------------------------------------
# COMMENTS MODEL
# -----------------------------------------------------


class Comment(models.Model):
    """
    Represents a comment or reply in the discussion.

    Comments are associated with a specific post and can be liked by users.
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    content = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)

    approved = models.BooleanField(default=True)

    @property
    def like_count(self):
        return self.likes.count()

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"

# -----------------------------------------------------
# VOTE/ LIKE MODEL
# -----------------------------------------------------


class Like(models.Model):
    """
    Represents a like (upvote) by a user on a post, comment, or resource.
    A like can be associated with exactly one of these content types.
    This allows users to show appreciation for helpful content and contributes
    to the reputation system.
    The unique_together constraint ensures a user can only like a specific
    Piece of content once.
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='likes'
    )

    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='likes'
    )

    resource = models.ForeignKey(
        Resource,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='likes'
    )

    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Prevents a user from liking twice
        unique_together = ('user', 'post', 'comment', 'resource')

    def clean(self):
        # Ensure that only one of post, comment, or resource is set
        targets = [self.post, self.comment, self.resource]
        if sum(target is not None for target in targets) != 1:
            raise ValidationError(
                "A like must be associated with exactly one of "
                "post, comment, or resource."
            )

    def __str__(self):
        return f"Like by {self.user}"


# auto create Profile when User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
