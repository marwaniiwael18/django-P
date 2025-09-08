
from django.contrib import admin
from django.urls import path
from .views import hello
from .views import bonjour

urlpatterns = [
    path('hi/', hello),
    path('bonjour/', bonjour),
]
