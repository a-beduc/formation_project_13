"""
Django app configuration for the 'lettings' app.

Classes:

    LettingsConfig
"""
from django.apps import AppConfig


class LettingsConfig(AppConfig):
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
    name = 'lettings'
