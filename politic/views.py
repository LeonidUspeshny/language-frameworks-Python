from django.shortcuts import render
from .models import Articles


def politic(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'politic/politic_home.html', {'news': news})
