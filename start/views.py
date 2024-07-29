from django.shortcuts import render



def start(request):
    return render(request, 'start/start.html')


def about(request):
    return render(request, 'start/about.html')
