from django.shortcuts import render
from .models import Post
# Create your views here.


def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html")
