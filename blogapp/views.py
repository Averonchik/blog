from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(date__lte=timezone.now()).order_by('date').reverse()
    return render(request, 'blogapp/post_list.html', {'posts': posts})


def post(request):
    # Отображение однго поста
    return render(request, 'blogapp/post.html')


def blog(request):
    # Отображение персонального блога
    return render(request, 'blogapp/blog.html')
