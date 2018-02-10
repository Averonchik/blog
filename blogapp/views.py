from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.mail import send_mail
from .models import Post, ProfileUser
from .forms import PostForm


# Create your views here.
def post_list(request):
    profiles, post_pk = [], []
    for profile in ProfileUser.objects.all():
        for sub in profile.subscribers.all():
            if request.user == sub.user:
                profiles.append(profile.user.pk)
        if profile.user == request.user:
            for pk in profile.read_posts.all():
                post_pk.append(pk.pk)
    posts = Post.objects.filter(author__pk__in=profiles) \
        .exclude(pk__in=post_pk).order_by('-date')
    return render(request, 'blogapp/post_list.html', {'posts': posts})


def post(request, pk):
    # Отображение одного поста
    p = get_object_or_404(Post, pk=pk)
    return render(request, 'blogapp/post_v.html', {'post': p})


def blog(request, pk):
    # Отображение персонального блога
    posts = Post.objects.filter(author=pk).order_by('date').reverse()
    author = get_object_or_404(User, pk=pk)
    return render(request, 'blogapp/blog.html',
                  {'posts': posts, 'author': author})


@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date = timezone.now()
            post.save()
            user = ProfileUser.objects.get(user=post.author)
            emails = []
            for sub in user.subscribers.all():
                emails.append(sub.user.email)
            send_mail(
                "В блоге у %s новый пост" % (post.author),
                "%s%s" % (get_current_site(request),
                          redirect('post', pk=post.pk).url),
                "yurgin.rodion@gmail.com", emails
            )
            return redirect('post', pk=post.pk)
        else:
            return redirect('/')
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
    user.profile.subscribers.add(request.user.profile)
    return redirect('/')


@login_required
def unfollow(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.profile.subscribers.remove(request.user.profile)
    return redirect('/')


@login_required
def read_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    request.user.profile.read_posts.add(post)
    return redirect('/')


@login_required
def unread_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    request.user.profile.read_posts.remove(post)
    return redirect('/')
