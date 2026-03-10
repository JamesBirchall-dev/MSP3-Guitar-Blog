
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Like, Resource, Profile, Subject
from django.db.models import Count, Q
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import (
    RegisterForm, PostForm, CommentForm, ResourceForm, ProfileForm
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json


@login_required
def verify_resource(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)
    profile = getattr(request.user, 'profile', None)
    if not profile or profile.role != 'teacher':
        return redirect(request.META.get("HTTP_REFERER", "index"))
    # Toggle verification
    resource.verified = not resource.verified
    resource.save()
    return redirect(request.META.get("HTTP_REFERER", "index"))


# TESTING AJAX
# @csrf_exempt
# def ajax_test(request):
#    if request.method == 'POST':
#        return JsonResponse({'message': 'AJAX request received!'})
#    return JsonResponse({'message': 'Send a POST request to test AJAX.'})


def index(request):
    # This view renders the main feed page (same as home)
    posts = Post.objects.filter(status=1).select_related(
        "subject", "author"
    ).annotate(likes_total=Count('likes')).order_by("-created_on")

    resources = Resource.objects.select_related(
        "subject", "added_by", "post"
    ).annotate(likes_total=Count('likes'))

    subject_slug = request.GET.get('subject')
    if subject_slug:
        posts = posts.filter(subject__slug=subject_slug)
        resources = resources.filter(subject__slug=subject_slug)

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

    content_type = request.GET.get('type')
    if content_type == 'post':
        resources = resources.none()
    elif content_type == 'resource':
        posts = posts.none()
    # Summernote: No markdown conversion needed; content is already HTML
    subjects = Subject.objects.all().order_by("name")

    context = {
        "posts": posts,
        "resources": resources,
        "subjects": subjects,
        "active_subject": subject_slug,
        "active_type": content_type,
        "query": query,
    }
    return render(request, "blog/index.html", context)


def base_view(request):
    return render(request, 'blog/base.html')


def subject_list_view(request):
    subjects = Subject.objects.annotate(
        post_count=Count('posts')
    ).order_by('name')
    return render(request, 'blog/subject_list.html', {'subjects': subjects})


# HOME PAGE VIEW
# Displays all published posts and resources

def home(request):
    posts = Post.objects.filter(status=1).select_related(
        "subject", "author"
    ).annotate(likes_total=Count('likes')).order_by("-created_on")

    resources = Resource.objects.select_related(
        "subject", "added_by", "post"
    ).annotate(likes_total=Count('likes'))


#  Subject Filter
    subject_slug = request.GET.get('subject')
    if subject_slug:
        posts = posts.filter(subject__slug=subject_slug)
        resources = resources.filter(subject__slug=subject_slug)

# search filter
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

# content ttype filter (post vs resource)
    content_type = request.GET.get('type')
    if content_type == 'post':
        resources = resources.none()  # Exclude resources
    elif content_type == 'resource':
        posts = posts.none()  # Exclude posts

    posts = posts.order_by("-created_on")
    resources = resources.order_by("-created_on")

    subjects = Subject.objects.all().order_by("name")

    context = {
        "posts": posts,
        "resources": resources,
        "subjects": subjects,
        "active_subject": subject_slug,
        "active_type": content_type,
        "query": query,

    }
    return render(request, "blog/index.html", context)


def post_detail(request, slug):
    from django.db.models import Count
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
                        Resource.objects.create(
                            comment=comment,
                            added_by=request.user,
                            title=resource_title,
                            url=resource_url,
                            description=resource_description or '',
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

    # makes sure a profile exists for the user, creates one if not
    profile, created = Profile.objects.get_or_create(user=user_obj)

    posts = user_obj.blog_posts.all().order_by("-created_on")
    comments = user_obj.comment_set.all().order_by("-created_on")
    resources = user_obj.resources.all().order_by("-created_on")

    context = {
        'profile_user': user_obj,
        'profile': profile,
        'posts': posts,
        'comments': comments,
        'resources': resources,
    }

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
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


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
        # Prevent users from liking their own posts
        return redirect(request.META.get("HTTP_REFERER", "index"))
    like, created = Like.objects.get_or_create(
        user=request.user,
        post=post
    )
    if not created:
        # User has already liked, so remove the like
        like.delete()
    return redirect(request.META.get("HTTP_REFERER", "index"))


# comment like view

@login_required
def like_comment(request, comment_id):
    if request.method != "POST":
        return redirect("home")
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author == request.user:
        # Prevent users from liking their own comments
        return redirect("post_detail", slug=comment.post.slug)
    like, created = Like.objects.get_or_create(
        user=request.user,
        comment=comment
    )

    if not created:
        # User has already liked, so remove the like
        like.delete()

    return redirect("post_detail", slug=comment.post.slug)


@login_required
def like_resource(request, resource_id):
    if request.method != "POST":
        return redirect("home")
    resource = get_object_or_404(Resource, id=resource_id)
    if resource.added_by == request.user:
        # Prevent users from liking their own resources
        if resource.post:
            return redirect("post_detail", slug=resource.post.slug)
        else:
            return redirect("index")
    like, created = Like.objects.get_or_create(
        user=request.user,
        resource=resource
    )

    if not created:
        # User has already liked, so remove the like
        like.delete()

    if resource.post:
        return redirect("post_detail", slug=resource.post.slug)
    else:
        return redirect("index")


# Subject detail view

def subject_detail_view(request, slug):
    subject = get_object_or_404(Subject, slug=slug)

    tag_slug = request.GET.get('tag')
    if tag_slug:
        posts = subject.posts.filter(tags__slug=tag_slug)
    else:
        posts = subject.posts.all()

    from django.db.models import Count
    posts = posts.annotate(likes_total=Count('likes')).order_by("-created_on")

    # Add resources for this subject, annotated with votes_total
    from django.db.models import Count
    resources = subject.resources.all()\
        .select_related("subject", "added_by", "post")\
        .annotate(likes_total=Count('likes'))

    tags = subject.tags.all()

    return render(request, 'blog/subject_detail.html', {
        'subject': subject,
        'posts': posts,
        'resources': resources,
        'tags': tags,
        'active_tag_slug': tag_slug,
    })
