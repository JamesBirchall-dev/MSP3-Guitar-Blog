from django.shortcuts import render, get_object_or_404
from .models import Post


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
