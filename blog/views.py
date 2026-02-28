from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Vote, Resource, Profile
from django.db.models import Count
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, PostForm, CommentForm, ResourceForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def base_view(request):
    return render(request, 'blog/base.html')


def subject_list_view(request):
    return render(request, 'blog/subject_list.html')


def home(request):
    posts = Post.objects.filter(status=1).order_by("-created_on")
    return render(request, "blog/index.html", {"posts": posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    # order comments by vote count and then by creation date
    comments = post.comments.annotate(
        vote_count=Count('votes')
    ).order_by('-vote_count', '-created_on')

    # Order resources by vote count then creation date
    resources = post.resources.annotate(
        vote_count=Count('votes')
    ).order_by('-vote_count', '-created_on')

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

# login/out and registration views


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
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
    # Allows logged-in users to create a post.
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Assign current user
            post.status = 1  # Set post as published
            post.save()
            return redirect("home")

    else:
        form = PostForm()

    return render(request, "blog/create_post.html", {"form": form})


# comment voting view

@login_required
def vote_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    vote, created = Vote.objects.get_or_create(
        user=request.user,
        comment=comment
    )

    if not created:
        # User has already voted, so remove the vote
        vote.delete()

    return redirect("post_detail", slug=comment.post.slug)


@login_required
def vote_resource(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)
    vote, created = Vote.objects.get_or_create(
        user=request.user,
        resource=resource
    )

    if not created:
        # User has already voted, so remove the vote
        vote.delete()

    return redirect("post_detail", slug=resource.post.slug)
