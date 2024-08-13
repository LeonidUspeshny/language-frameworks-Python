from django.shortcuts import render


def sport(request):
    return render(request, 'sport/sport_home.html')

# Create your views here.
