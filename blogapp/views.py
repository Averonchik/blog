from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(date__lte=timezone.now()).order_by('date').reverse()
    return render(request, 'blogapp/post_list.html', {'posts': posts})


def post(request, pk):
    # Отображение однго поста
    p = get_object_or_404(Post, pk=pk)
    return render(request, 'blogapp/post.html', {'post': p})


def blog(request, pk):
    # Отображение персонального блога
    posts = get_list_or_404(Post.objects.order_by('date').reverse(), author=pk)
    author = get_object_or_404(User, pk=pk)
    return render(request, 'blogapp/blog.html', {'posts': posts, 'author': author})
