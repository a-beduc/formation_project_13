"""
Django admin panel configuration for the 'profiles' app.
"""
from django.contrib import admin

from .models import Profile

admin.site.register(Profile)
