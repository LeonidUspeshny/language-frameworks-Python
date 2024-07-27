from django.urls import path
from . import views


urlpatterns = [
    path('', views.start, name='Start'),
    path('about', views.about),
    path('lessons', views.lessons),
    path('works', views.works),


]