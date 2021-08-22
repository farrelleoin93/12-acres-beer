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

    blog = get_object_or_404(Post, slug=slug)

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog_detail.html', context)


@login_required
def add_blog(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only 12 Acres owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            messages.success(request, 'Successfully added blog!')
            return redirect(reverse('_detail', args=[blog.slug]))
        else:
            messages.error(request, 'Failed to add beer. Please ensure the form is valid.')
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

