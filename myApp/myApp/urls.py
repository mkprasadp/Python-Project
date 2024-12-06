from django.contrib import admin
from django.urls import path
from .views import Home,Loginpage,Registration,submit_form

urlpatterns = [
    path('submit/', submit_form, name='submit_form'),
    path('Home/',Home,name='Home'),
    path('Loginpage/',Loginpage, name='Loginpage'),
    path('Registration/',Registration,name='Registration')
]