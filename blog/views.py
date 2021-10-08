from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm
# Create your views here.


def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html")


# def create_post(request):
#     post = PostForm()
#     if request.method == 'POST':
#         post = PostForm(request.POST)

#         if post.is_valid():
#             post.save()
#             messages.success(request, f"Post Created!!")
#             return redirect("/blog")
#     context = {'post': post}
#     return render(request, 'blog/post.html', context)
