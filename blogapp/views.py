from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Post
from .forms import PostForm


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(date__lte=timezone.now()).order_by('date').reverse()
    return render(request, 'blogapp/post_list.html', {'posts': posts})


def post(request, pk):
    # Отображение однго поста
    p = get_object_or_404(Post, pk=pk)
    return render(request, 'blogapp/post_v.html', {'post': p})


def blog(request, pk):
    # Отображение персонального блога
    posts = Post.objects.filter(author__lte=pk).order_by('date').reverse()
    author = get_object_or_404(User, pk=pk)
    return render(request, 'blogapp/blog.html', {'posts': posts, 'author': author})


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date = timezone.now()
            post.save()
        return redirect('post', pk=post.pk)
    else:
        form = PostForm
        return render(request, 'blogapp/new_post.html', {'form': form})


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        return redirect('post_list')
    else:
        form = PostForm(instance=post)
        return render(request, 'blogapp/new_post.html', {'form': form})


@login_required
def follow(request, pk):
    user = get_object_or_404(User, pk=pk)
    request.user.profile.subscribers.add(user.profile)
    return redirect('/')


@login_required
def read_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    request.user.profile.read_posts.add(post)
    return redirect('/')
