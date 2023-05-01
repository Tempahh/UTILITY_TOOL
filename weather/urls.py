from . import views
from django.urls import path

urlpatterns = [
    path('',  views.index, name='index'),# type: ignore
    path('weather', views.weather, name='weather'),
    path('login', views.loginpage, name='login'),
    path('register', views.register, name='register'),
]