from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls.base import reverse

from .forms import UserForm, Login


def register(request):
    user_form = UserForm()
    if request.POST:
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            username, email, password = user_form.cleaned_data['username'], \
                user_form.cleaned_data['email'], \
                user_form.cleaned_data['password']
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.is_active = True
            user.save()
        messages.success(request, "Register ok")
        return redirect('/')
    return render(request, 'register.html', {
        'user_form': user_form,
    })


def log_in(request):
    login_form = Login()
    if request.POST:
        login_form = Login(request.POST)
        if login_form.is_valid():
            user = authenticate(
                username=login_form.cleaned_data['username'],
                password=login_form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
            messages.success(request, 'Login ok')
            return redirect(request.GET.get('next', '/'))
    return render(request, 'login.html', {
        'login_form': login_form
    })


def log_out(request):
    logout(request)
    return redirect(reverse('root'))