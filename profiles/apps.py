"""
Django app configuration for the 'profiles' app.

Classes:

    ProfileConfig
"""
from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    A class to add specific configuration variables to the Django app.

    Attributes
    ----------
    default_auto_field : str
        The default auto-field to use when creating new objects.
    name : str
        The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
