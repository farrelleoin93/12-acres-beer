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

    blog_detail = get_object_or_404(Post, slug=slug)

    template = 'blog/blog_detail.html'
    context = {
        'blog_detail': blog_detail,
    }

    return render(request, template, context)


@login_required
def add_blog(request):
    """ Add a new blog post """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only 12 Acres owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog_detail = form.save()
            messages.success(request, 'Successfully added a new Blog Post.')
            return redirect(
                reverse('blog_detail', args=[blog_detail.slug]))
        else:
            messages.error(
                request,
                'Failed to add a Blog Post. Please ensure the form is valid.')
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, slug):
    """ Edit a blog post """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only 12 Acres owners can do that.')
        return redirect(reverse('home'))

    blog_detail = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog_detail)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Blog Post.')
            return redirect(reverse('blog_detail', args=[blog_detail.slug]))
        else:
            messages.error(
                request,
                'Failed to edit Blog Post. Please ensure the form is valid.')
    else:
        form = BlogForm(instance=blog_detail)
        messages.info(request, f'You are editing {blog_detail.title}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blog_detail': blog_detail,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, slug):
    """ Delete an existing blog post """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('home'))

    blog_detail = get_object_or_404(Post, slug=slug)
    blog_detail.delete()

    messages.success(
        request, 'The selected blog post has '
        'successfully been deleted.')
    return redirect(reverse('blog'))
