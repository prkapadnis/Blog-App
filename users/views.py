from typing import ContextManager
from django.db.models.query import InstanceCheckMeta
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistration, UserUpdateForm, ProfileUpdateForm, BioUpdateForm


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


def edit_profile(request):
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    bio_form = BioUpdateForm(instance=request.user.bio)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        bio_form = BioUpdateForm(request.POST, instance=request.user.bio)
        if u_form.is_valid() and p_form.is_valid() and bio_form.is_valid():
            u_form.save()
            p_form.save()
            bio_form.save()
            messages.success(request, f'Your account has been updated!!')
    context = {'form': u_form, 'profile': p_form, 'bio': bio_form}
    return render(request, "users/edit_profile.html", context)
