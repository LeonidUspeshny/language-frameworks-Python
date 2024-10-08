from django.contrib import admin
from django.urls import path
from Register.views import register, user_login, user_logout
# from News.views import HomeNews, NewsByCategory, AddNews

urlpatterns = [
    # path('', HomeNews.as_view(), name='Home'),
    # path('category/<int:category_id>/', NewsByCategory.as_view(), name='Category'),
    # path('news/<int:pk>/', NewsByCategory.as_view(), name='View_news'),
    # path('news/add_news', AddNews.as_view(), name='Add_news'),
    path('register', register, name='Register'),
    path('', register, name='Register'),
    path('login', user_login, name='Login'),
    path('logout', user_logout, name='Logout'),
]