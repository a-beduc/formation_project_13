"""
Django urls for the 'oc_lettings_site' app.

Misc variables:
    urlpatterns
"""

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('lettings/', include(('lettings.urls', 'lettings'),
                              namespace='lettings')),
    path('profiles/', include(('profiles.urls', 'profiles'),
                              namespace='profiles')),

]
