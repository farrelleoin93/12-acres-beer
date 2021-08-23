from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post

from .forms import BlogForm


def blog(request):

    posts = Post.objects.all()

    template = 'blog/blog.html'
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def blog_detail(request, slug):
    """ A view to show blog details """

    post = get_object_or_404(Post, slug=slug)

    template = 'blog/blog_detail.html'
    context = {
        'post': post,
    }

    return render(request, template, context)


def add_blog(request):
    form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
