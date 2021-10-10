from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import PostForm
# Create your views here.


def home(request):
    posts = Post.objects.all().order_by('-dateOfPosted')
    context = {'posts': posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html")


@login_required(login_url="/user/")
def createPost_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            form = PostForm()
            messages.success(request, "The Post is created!!")
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'blog/post.html', context)


def postDetail_view(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, "blog/postDetails_view.html", context)
