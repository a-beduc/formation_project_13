"""
Django tests for the 'lettings/models.py' file.

Functions:
    test_address_str(address_fixture) -> None
    test_letting_str(letting_fixture) -> None
    test_letting_create_fail_address_already_attributed(letting_fixture)
    -> None
"""
import pytest
from django.db import IntegrityError

from lettings.models import Address, Letting


@pytest.mark.django_db
def test_address_str(address_fixture):
    """
    Test if the Address.__str__() method works as expected.

        Parameters:
            address_fixture (Address): An Address instance.

        Returns:
            None
    """
    address = Address.objects.get(id=1)
    assert str(address) == f"{address_fixture.number} {address_fixture.street}"


@pytest.mark.django_db
def test_letting_str(letting_fixture):
    """
    Test if the Letting.__str__() method works as expected.

        Parameters:
            letting_fixture (Letting): A Letting instance.

        Returns:
            None
    """
    letting = Letting.objects.get(id=1)
    assert str(letting) == f"{letting_fixture.title}"


@pytest.mark.django_db
def test_letting_create_fail_address_already_attributed(letting_fixture):
    """
    Test if creating a Letting with an address that is already linked
    to another Letting throw an Error.

        Parameters:
            letting_fixture (Letting): A Letting instance.

        Returns:
            None
    """
    data = {
        "title": "new_dummy",
        "address": Address.objects.get(id=1),
    }
    with pytest.raises(IntegrityError,
                       match="UNIQUE constraint failed: "
                             "lettings_letting.address_id"):
        Letting.objects.create(**data)
