from django.shortcuts import render
from django.http import HttpResponse


def start(request):
    return HttpResponse("<h4>Проверка работы</h4>")


def about(request):
    return HttpResponse("<h4>Страница про нас</h4>")


def lessons(request):
    return HttpResponse("<h4>Мои занятия</h4>")


def works(request):
    return HttpResponse("<h4>Мои работы</h4>")
# Create your views here.
