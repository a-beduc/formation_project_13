"""
Django urls for the 'lettings' app.

Misc variables:
    app_name
    urlpatterns
"""
from django.urls import path

from . import views

app_name = 'lettings'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
