from django.shortcuts import render


def start(request):
    data = {'title': 'Стартовая страница', 'values': ['Some', 'Helo', '123'],
    'obj': {
        'car': 'BMW',
        'age': 18,
        'hobby': 'Football'
    }
    }
    return render(request, 'start/start.html', data)


def about(request):
    return render(request, 'start/about.html')
