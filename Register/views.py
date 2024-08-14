from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            form.save()
            messages.success(request, 'Your registration is success')
            return redirect('Login')
        else:
            messages.error(request, 'Registration error!')
    else:
        form = UserCreationForm()
    return render(request, 'Register/register.html', {'form': form})


def login(request):
    return render(request, 'Register/login.html')

