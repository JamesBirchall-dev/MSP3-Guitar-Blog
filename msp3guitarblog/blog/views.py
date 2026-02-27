from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from .forms import RegisterForm, PostForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'blog/index.html')


def post_detail(request, slug):
    # status=1 means Published
    post = get_object_or_404(Post, slug=slug, status=1)
    return render(request, 'blog/post_detail.html', {'post': post})


def base_view(request):
    return render(request, 'blog/base.html')


def create_post_view(request):
    return render(request, 'blog/create_post.html')


def subject_list_view(request):
    return render(request, 'blog/subject_list.html')


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
