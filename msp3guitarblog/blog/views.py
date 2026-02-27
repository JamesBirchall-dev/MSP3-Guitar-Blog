from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, PostForm, CommentForm
from django.contrib.auth.decorators import login_required


def base_view(request):
    return render(request, 'blog/base.html')


def subject_list_view(request):
    return render(request, 'blog/subject_list.html')


def home(request):
    posts = Post.objects.filter(status=1).order_by("-created_on")
    return render(request, "blog/index.html", {"posts": posts})


def post_detail(request, slug):
    # get specific post by slug or return 404 if not found
    post = get_object_or_404(Post, slug=slug)

# get all approved comments for this post
    comments = post.comments.filter(approved=True).order_by("-created_on")

    # if user submits a comment form
    if request.method == "POST":

        # create a comment form instance with submitted data
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid() and request.user.is_authenticated:

            # dont save to db yet, we need to assign post and author first
            new_comment = comment_form.save(commit=False)

            # attach post and author to comment
            new_comment.post = post

            new_comment.author = request.user

            # save comment to db
            new_comment.save()

            # redirect to same post detail page to show new comment
            return redirect("post_detail", slug=post.slug)

    context = {
        "post": post,
        "comments": comments,
        "comment_form": CommentForm()
    }
    return render(request, "blog/post_detail.html", context)

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
            post.save()
            return redirect("home")

    else:
        form = PostForm()

    return render(request, "blog/create_post.html", {"form": form})
