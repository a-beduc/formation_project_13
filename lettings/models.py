"""
Django models for the 'lettings' app.

Classes:

    Address
    Letting
"""

from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


class Address(models.Model):
    """
    A class to represent an address.

    Attributes
    ----------
    number : int
        The number of the address.
    street : str
        The street name of the address.
    city : str
        The city of the address.
    state : str
        The state of the address.
    zip_code : int
        The zip code of the address.
    country_iso_code : str
        The country iso code of the address.

    Methods
    -------
    __str__():
        Returns the string representation of the address.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """ Returns the string representation of the address. """
        return f'{self.number} {self.street}'

    class Meta:
        verbose_name_plural = 'Addresses'


class Letting(models.Model):
    """
    A class to represent a letting.

    Attributes
    ----------
    title : str
        The title of letting.
    address : Address
        The physical address of the letting.

    Methods
    -------
    __str__():
        Returns the string representation of the address.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """ Returns the string representation of the address. """
        return self.title
