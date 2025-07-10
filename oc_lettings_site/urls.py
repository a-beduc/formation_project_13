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

handler404 = 'oc_lettings_site.views.custom_page_not_found_view'
handler500 = 'oc_lettings_site.views.custom_error_view'
