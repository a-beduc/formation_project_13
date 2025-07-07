"""
Pytest fixtures for tests of the 'profiles' app.

Functions:
    user_fixture() -> User
    profile_fixture(user_fixture) -> Profile
"""
import pytest
from django.contrib.auth.models import User

from profiles.models import Profile


@pytest.fixture
def user_fixture():
    """
    Return and save in a fake database a User instance.

        Returns:
            User : A User instance.
    """
    data = {
        "username": "test_user",
        "password": "Password1",
        "first_name": "test_first_name",
        "last_name": "test_last_name",
        "email": "test_email",
    }
    return User.objects.create_user(**data)


@pytest.fixture
def profile_fixture(user_fixture):
    """
    Return and save in a fake database a Profile instance.

        Parameters:
            user_fixture (User): A User instance.

        Returns:
            Profile : A Profile instance.
    """
    data = {
        "user": user_fixture,
        "favorite_city": "dummy",
    }
    return Profile.objects.create(**data)
