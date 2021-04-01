from django.contrib import admin
from django.urls import path, include
from .views import home, about, billing

urlpatterns = [
    path('', home, name='home'),
    path('about/', home, name='about'),
    path('billing/', billing, name='billing'),
]