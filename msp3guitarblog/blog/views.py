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
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(
        parent__isnull=True
    ).order_by("-created_on")

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid() and request.user.is_authenticated:
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user

            parent_id = request.POST.get('parent_id')
            if parent_id:
                from .models import Comment
                try:
                    new_comment.parent = Comment.objects.get(id=parent_id)
                except Comment.DoesNotExist:
                    new_comment.parent = None

            new_comment.save()
            return redirect("post_detail", slug=post.slug)
    else:
        comment_form = CommentForm()

    context = {
        "post": post,
        "comments": comments,
        "comment_form": comment_form
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
