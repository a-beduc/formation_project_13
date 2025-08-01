"""
Django urls for the 'profiles' app.

Misc variables:
    app_name
    urlpatterns
"""
from django.urls import path

from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
]
