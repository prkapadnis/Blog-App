from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistration


def register_view(request):
    user_form = UserRegistration()
    if request.method == "POST":
        user_form = UserRegistration(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(
                request, "Your account created successfully!! You can log in now...")
    context = {'form': user_form}
    return render(request, "users/register.html", context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/blog')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid Username or Password')
        else:
            messages.error(request, 'Invalid Username or Password')
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, "users/login.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')


def profile_view(request):
    return render(request, "users/profile.html")
