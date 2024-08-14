from django.contrib import admin
from django.urls import path
from Register.views import register, login

urlpatterns = [
    path('', register, name='Register'),
    path('login', login, name='Login'),
]