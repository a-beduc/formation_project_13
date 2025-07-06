"""
Django models for the 'profiles' app.

Classes:

    Profile
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    A class to represent a profile.

    Attributes
    ----------
    user : User
        The title of letting.
    favorite_city : str
        The name of a city.

    Methods
    -------
    __str__():
        Returns the string representation of the address.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """ Returns the string representation of the address. """
        return self.user.username
