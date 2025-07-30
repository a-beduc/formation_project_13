"""
Django admin panel configuration for the 'lettings' app.
"""
from django.contrib import admin

from .models import Address
from .models import Letting

admin.site.register(Letting)
admin.site.register(Address)
