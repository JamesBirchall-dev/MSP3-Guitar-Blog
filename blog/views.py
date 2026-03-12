"""
Views for the Guitar Learning Blog application.

This file contains all controller logic for the site, including:

• Feed generation (home/index)
• Post detail and discussion threads
• User profiles
• Post / comment / resource CRUD operations
• Like/voting functionality
• Subject browsing and filtering
• Authentication (register/login/logout)
• AJAX endpoints for dynamic UI updates

The views coordinate between:
- Models (database structure)
- Forms (user input)
- Templates (presentation layer)
"""

# Django shortcuts for common view operations
from django.shortcuts import render, get_object_or_404, redirect

# Used for returning AJAX responses
from django.http import JsonResponse

# Application models
from .models import Post, Comment, Like, Resource, Profile, Subject, Tag

# Query utilities for aggregation and complex filtering
from django.db.models import Count, Q

# Authentication utilities
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Application forms
from .forms import (
    RegisterForm, PostForm, CommentForm, ResourceForm, ProfileForm
)

# Pagination utilities
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Used for AJAX data serializati
import json

# Restricts a view to GET requests only
from django.views.decorators.http import require_GET


# -----------------------------------------------------
# HOME ROUTING VIEW
# -----------------------------------------------------

def home(request):

    """
    Root URL view.

    This function simply forwards the request to the
    main feed view (`index`). This allows the homepage
    route to remain clean while keeping feed logic
    centralized in a single function.
    """

    return index(request)


@login_required
def verify_resource(request, resource_id):
    """
    Allows teachers to verify or unverify a learning resource.

    Verification is used to highlight trusted resources added
    by the community. Only users with the 'teacher' role can
    toggle verification status.

    Behaviour:
    • Finds the resource by ID
    • Confirms the logged-in user is a teacher
    • Toggles the verified flag
    • Redirects back to the referring page
    """

    resource = get_object_or_404(Resource, id=resource_id)
    profile = getattr(request.user, 'profile', None)
    if not profile or profile.role != 'teacher':
        return redirect(request.META.get("HTTP_REFERER", "index"))
    # Toggle verification
    resource.verified = not resource.verified
    resource.save()
    return redirect(request.META.get("HTTP_REFERER", "index"))


# -----------------------------------------------------
# MAIN FEED VIEW (INDEX)
# -----------------------------------------------------


def index(request):
    """
    Main homepage feed displaying posts and resources.

    The feed combines two content types:
    • Posts (learning articles created by teachers)
    • Resources (community shared learning materials)

    Features implemented in this view:

    - Filtering by subject
    - Filtering by tag
    - Full text search
    - Content type filtering (posts vs resources)
    - Combined chronological feed
    - Pagination
    - Like status detection
    - AJAX partial rendering

    The feed is constructed by:
    1. Querying posts and resources separately
    2. Applying filters to each queryset
    3. Converting them into a unified list
    4. Sorting by creation date
    5. Paginating the combined results
    """

    posts = Post.objects.filter(status=1).select_related(
        "subject", "author"
    ).annotate(likes_total=Count('likes')).order_by("-created_on")

    resources = Resource.objects.select_related(
        "subject",
        "added_by",
        "post"
    ).annotate(likes_total=Count('likes'))

    # -------------------------------------------------
    # FEED FILTERING
    # -------------------------------------------------

    # Filter by subject if provided
    subject_slug = request.GET.get('subject')
    if subject_slug:
        posts = posts.filter(subject__slug=subject_slug)
        resources = resources.filter(subject__slug=subject_slug)

    # Filter by tags if provided (supports multiple tags)
    tag_slug = request.GET.getlist('tag')
    if tag_slug:
        posts = posts.filter(tags__slug__in=tag_slug)

    # Filter by search query if provided
    query = request.GET.get('q')
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )
        resources = resources.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    # Filter by content type if specified
    content_type = request.GET.get('type')
    if content_type == 'post':
        resources = resources.none()
    elif content_type == 'resource':
        posts = posts.none()

    # Now convert to lists and combine
    posts = list(posts)
    for post in posts:
        post.item_type = 'post'

    resources = list(resources)
    for resource in resources:
        resource.item_type = 'resource'

    combined_feed = posts + resources
    combined_feed.sort(key=lambda x: x.created_on, reverse=True)

    # -------------------------------------------------
    # PAGINATION
    # -------------------------------------------------

    page = request.GET.get('page', 1)
    paginator = Paginator(combined_feed, 10)
    try:
        feed = paginator.page(page)
    except PageNotAnInteger:
        feed = paginator.page(1)
    except EmptyPage:
        feed = paginator.page(paginator.num_pages)

    # Like/unlike functionality for paginated feed
    if request.user.is_authenticated:
        for item in combined_feed:
            if item.item_type == 'post':
                item.user_has_liked = item.likes.filter(
                    user=request.user
                ).exists()
            elif item.item_type == 'resource':
                item.user_has_liked = item.likes.filter(
                    user=request.user
                ).exists()

    subjects = Subject.objects.all().order_by("name")

    # Build subject-tag dictionary for AJAX
    subject_tags = {
        str(subject.pk): [tag.name for tag in subject.tags.all()]
        for subject in subjects
    }

    tags = Tag.objects.all()
    context = {
        "feed": feed,
        "subjects": subjects,
        "active_subject": subject_slug,
        "active_type": content_type,
        "query": query,
        "subject_tags_json": json.dumps(subject_tags),
        "tags": tags,
    }
    # If request was made via AJAX, return only feed items
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, "blog/_feed_items.html", context)
    # Otherwise render full page
    return render(request, "blog/index.html", context)


def post_detail(request, slug):
    post = get_object_or_404(
        Post.objects.annotate(likes_total=Count('likes')),
        slug=slug
    )

    # order comments by like count and then by creation date
    comments = post.comments.annotate(
        likes_total=Count('likes')
    ).order_by('-likes_total', '-created_on')

    # Order resources by like count then creation date
    resources = post.resources.annotate(
        likes_total=Count('likes')
    ).order_by('-likes_total', '-created_on')

    if request.user.is_authenticated:
        post.user_has_liked = Like.objects.filter(
            user=request.user,
            post=post
        ).exists()
        for comment in comments:
            comment.user_has_liked = Like.objects.filter(
                user=request.user,
                comment=comment
            ).exists()
        for resource in resources:
            resource.user_has_liked = Like.objects.filter(
                user=request.user,
                resource=resource
            ).exists()

    comment_form = CommentForm()
    resource_form = ResourceForm()
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect("login")
        # comment section
        if "content" in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user

                comment.post = post
                comment.save()

                # Check if resource fields are filled
                resource_title = (
                    comment_form.cleaned_data.get('resource_title')
                )
                resource_url = (
                    comment_form.cleaned_data.get('resource_url')
                )
                resource_description = (
                    comment_form.cleaned_data.get(
                        'resource_description'
                    )
                )
                if resource_title or resource_url or resource_description:
                    if resource_title and resource_url:
                        resource, created = Resource.objects.get_or_create(
                            comment=comment,
                            post=post,
                            added_by=request.user,
                            title=resource_title,
                            url=resource_url,
                            description=resource_description or "",
                        )

            return redirect("post_detail", slug=slug)

    # Summernote: No markdown conversion needed; content is already HTML

    context = {
        "post": post,
        "comments": comments,
        "resources": resources,
        "comment_form": comment_form,
        "resource_form": resource_form
    }
    return render(request, "blog/post_detail.html", context)


def profile_view(request, username):
    user_obj = get_object_or_404(User, username=username)
    profile, created = Profile.objects.get_or_create(user=user_obj)

    posts = user_obj.blog_posts.all().annotate(
        likes_total=Count('likes')
    ).order_by("-created_on")
    resources = user_obj.resources.all().annotate(
        likes_total=Count('likes')
    ).order_by("-created_on")

    # Filtering
    subject_slug = request.GET.get('subject')
    if subject_slug:
        posts = posts.filter(subject__slug=subject_slug)
        resources = resources.filter(subject__slug=subject_slug)
    tag_slugs = request.GET.getlist('tag')
    if tag_slugs:
        posts = posts.filter(tags__slug__in=tag_slugs)
    query = request.GET.get('q')
    content_type = request.GET.get('type')
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )
        resources = resources.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )
    if content_type == 'post':
        resources = resources.none()
    elif content_type == 'resource':
        posts = posts.none()

    posts = list(posts)
    for post in posts:
        post.item_type = 'post'
    resources = list(resources)
    for resource in resources:
        resource.item_type = 'resource'

    combined_feed = posts + resources
    combined_feed.sort(
        key=lambda x: x.created_on,
        reverse=True
    )

    # Remove duplicates for comments and resources
    unique_feed = []
    seen_ids = set()
    for item in combined_feed:
        unique_id = getattr(item, 'id', None)
        if unique_id and unique_id not in seen_ids:
            unique_feed.append(item)
            seen_ids.add(unique_id)
    combined_feed = unique_feed

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(combined_feed, 10)
    try:
        feed = paginator.page(page)
    except PageNotAnInteger:
        feed = paginator.page(1)
    except EmptyPage:
        feed = paginator.page(paginator.num_pages)

    # Like/unlike functionality
    if request.user.is_authenticated:
        for item in combined_feed:
            item.user_has_liked = item.likes.filter(user=request.user).exists()

    subjects = Subject.objects.all().order_by("name")
    # Build subject-tag dictionary for AJAX (same as index)
    subject_tags = {
        str(subject.pk): [tag.name for tag in subject.tags.all()]
        for subject in subjects
    }
    tags = Tag.objects.all()
    context = {
        'profile_user': user_obj,
        'profile': profile,
        'feed': feed,
        'query': query,
        'active_type': content_type,
        'tags': tags,
        'selected_tags': tag_slugs,
        'subjects': subjects,
        'active_subject': subject_slug,
        'subject_tags_json': json.dumps(subject_tags),
    }
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, "blog/_feed_items.html", context)
    return render(request, 'blog/profile.html', context)


# profile update view

@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'blog/edit_profile.html', {'form': form})


# login/out and registration views


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Set the role in the Profile
            role = form.cleaned_data.get('role', 'beginner')
            if hasattr(user, 'profile'):
                user.profile.role = role
                user.profile.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')


# restrict post creation to logged-in users

@login_required
def create_post(request):

    # ensures user has a profile
    profile, created = Profile.objects.get_or_create(user=request.user)

    # only allow users with a role of 'teacher'
    if profile.role != 'teacher':
        return redirect('home')

    # Allows logged-in users to create a post.
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Assign current user
            post.status = 1  # Set post as published
            post.save()
            form.save_m2m()  # Save tags
            return redirect("home")

    else:
        form = PostForm()
        # Build subject-tag dictionary
    subject_tags = {
        str(subject.pk): [tag.name for tag in subject.tags.all()]
        for subject in Subject.objects.all()
    }
    subject_tags_json = json.dumps(subject_tags)

    # Pass to template context
    context = {
        'form': form,
        'subject_tags_json': subject_tags_json,
    }
    return render(request, "blog/create_post.html", context)


# --- POST EDIT/DELETE ---
@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.author != request.user:
        return redirect('post_detail', slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})


@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.author != request.user:
        return redirect('post_detail', slug=slug)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, 'blog/delete_post.html', {'post': post})


# --- COMMENT EDIT/DELETE ---
@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.author != request.user:
        return redirect('post_detail', slug=comment.post.slug)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=comment.post.slug)
    else:
        form = CommentForm(instance=comment)
    return render(
        request,
        'blog/edit_comment.html',
        {'form': form, 'comment': comment}
    )


@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.author != request.user:
        return redirect('post_detail', slug=comment.post.slug)
    if request.method == 'POST':
        comment.delete()
        return redirect('post_detail', slug=comment.post.slug)
    return render(request, 'blog/delete_comment.html', {'comment': comment})


# --- RESOURCE EDIT/DELETE ---
@login_required
def edit_resource(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    if resource.added_by != request.user:
        return redirect('post_detail', slug=resource.post.slug)
    if request.method == 'POST':
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=resource.post.slug)
    else:
        form = ResourceForm(instance=resource)
    return render(
        request,
        'blog/edit_resource.html',
        {'form': form, 'resource': resource}
    )


@login_required
def delete_resource(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    if resource.added_by != request.user:
        return redirect('post_detail', slug=resource.post.slug)
    if request.method == 'POST':
        resource.delete()
        return redirect('post_detail', slug=resource.post.slug)
    return render(request, 'blog/delete_resource.html', {'resource': resource})

# Post voting view


@login_required
def like_post(request, post_id):
    if request.method != "POST":
        return redirect("home")
    post = get_object_or_404(Post, id=post_id)
    if post.author == request.user:
        return redirect(request.META.get("HTTP_REFERER", "index"))
    like, created = Like.objects.get_or_create(
        user=request.user,
        post=post
    )
    if not created:
        like.delete()
    liked = Like.objects.filter(user=request.user, post=post).exists()
    like_count = post.likes.count()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'liked': liked, 'like_count': like_count})
    return redirect(request.META.get("HTTP_REFERER", "index"))


# comment like view

@login_required
def like_comment(request, comment_id):
    if request.method != "POST":
        return redirect("home")
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author == request.user:
        return redirect("post_detail", slug=comment.post.slug)
    like, created = Like.objects.get_or_create(
        user=request.user,
        comment=comment
    )
    if not created:
        like.delete()
    liked = Like.objects.filter(user=request.user, comment=comment).exists()
    like_count = comment.likes.count()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'liked': liked, 'like_count': like_count})
    return redirect("post_detail", slug=comment.post.slug)


@login_required
def like_resource(request, resource_id):
    if request.method != "POST":
        return redirect("home")
    resource = get_object_or_404(Resource, id=resource_id)
    if resource.added_by == request.user:
        return redirect(request.META.get("HTTP_REFERER", "index"))
    like, created = Like.objects.get_or_create(
        user=request.user,
        resource=resource
    )
    if not created:
        like.delete()
    liked = Like.objects.filter(user=request.user, resource=resource).exists()
    like_count = resource.likes.count()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'liked': liked, 'like_count': like_count})
    return redirect(request.META.get("HTTP_REFERER", "index"))


# Subject detail view

def subject_detail_view(request, slug):
    subject = get_object_or_404(Subject, slug=slug)

    tag_slugs = request.GET.getlist('tag')
    posts = subject.posts.filter(status=1)
    resources = subject.resources.all().select_related(
        "subject", "added_by", "post"
    )
    query = request.GET.get('q')
    content_type = request.GET.get('type')

    # If tag filter show only posts matching tags
    if tag_slugs and not content_type:
        posts = posts.filter(tags__slug__in=tag_slugs)
        resources = resources.none()
    else:
        if tag_slugs:
            posts = posts.filter(tags__slug__in=tag_slugs)
        if query:
            posts = posts.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            )
            resources = resources.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )
        if content_type == 'post':
            resources = resources.none()
        elif content_type == 'resource':
            posts = posts.none()

    posts = posts.annotate(likes_total=Count('likes')).order_by("-created_on")
    resources = resources.annotate(likes_total=Count('likes'))

    posts = list(posts)
    for post in posts:
        post.item_type = 'post'
    resources = list(resources)
    for resource in resources:
        resource.item_type = 'resource'

    combined_feed = posts + resources
    combined_feed.sort(
        key=lambda x: x.created_on,
        reverse=True
    )

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(combined_feed, 10)
    try:
        feed = paginator.page(page)
    except PageNotAnInteger:
        feed = paginator.page(1)
    except EmptyPage:
        feed = paginator.page(paginator.num_pages)

    # Like/unlike functionality
    if request.user.is_authenticated:
        for item in combined_feed:
            item.user_has_liked = item.likes.filter(user=request.user).exists()

    tags = subject.tags.all()

    active_tag_slug = tag_slugs[0] if tag_slugs else None
    context = {
        'subject': subject,
        'feed': feed,
        'tags': tags,
        'active_tag_slug': active_tag_slug,
        'query': query,
        'active_type': content_type,
    }

    # If request was made via AJAX, return only feed items
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, "blog/_feed_items.html", context)
    return render(request, 'blog/subject_detail.html', context)


def subject_list_view(request):
    from django.db.models import Q
    subjects = Subject.objects.annotate(
        post_count=Count('posts', filter=Q(posts__status=1), distinct=True),
        resource_count=Count('resources', distinct=True)
    ).order_by('name')
    return render(request, 'blog/subject_list.html', {'subjects': subjects})


def base_view(request):
    return render(request, 'blog/base.html')


@require_GET
def get_subject_tags(request):
    subject_id = request.GET.get('subject_id')
    if not subject_id:
        return JsonResponse({'tags': []})
    try:
        subject = Subject.objects.get(pk=subject_id)
        tags = [tag.name for tag in subject.tags.all()]
    except Subject.DoesNotExist:
        tags = []
    return JsonResponse({'tags': tags})
