from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

from .forms import NewsForm, UserRegisterForm, UserLoginForm
from django.contrib.auth import  login, logout


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm()
        if form.is_valid():
            form.save()
            messages.success(request, 'Your registration is success')
            user = form.save()
            login(request, user)
        else:
            messages.error(request, 'Registration error!')
    else:
        form = UserRegisterForm()
    return render(request, 'Register/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Home')
    else:
        form = UserLoginForm()
    return render(request, 'Register/login.html', {'form': form})


class AddNews(CreateView):
    form_class = NewsForm
    template_name = 'News/add_news.html'
    login_url = '/admin/'


def user_logout(request):
    logout(request)
    return redirect('Login')