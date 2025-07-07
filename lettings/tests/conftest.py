"""
Pytest fixtures for tests of the 'lettings' app.

Functions:
    address_fixture() -> Address
    letting_fixture() -> Letting
"""
import pytest

from lettings.models import Address, Letting


@pytest.fixture
def address_fixture():
    """
    Return and save in a fake database an Address instance.

        Returns:
            Address : An Address instance.
    """
    data = {
        'number': 4,
        'street': 'dummy',
        'city': 'dummy',
        'state': 'du',
        'zip_code': 4,
        'country_iso_code': 'dum',
    }
    return Address.objects.create(**data)


@pytest.fixture
def letting_fixture(address_fixture):
    """
    Return and save in a fake database a Letting instance.

        Parameters:
            address_fixture (Address): An Address instance.

        Returns:
            Letting : A Letting instance.
    """
    data = {
        "title": "dummy",
        "address": Address.objects.get(id=1),
    }
    return Letting.objects.create(**data)
