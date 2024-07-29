from django.urls import path
from . import views


urlpatterns = [
    path('', views.start, name='Start'),
    path('about', views.about),

]