"""
Django tests for the 'profiles/models.py' file.

Functions:
    user_fixture() -> User
    profile_fixture(user_fixture) -> Profile
    test_profile_str(profile_fixture) -> None
    test_profile_create_fail_user_already_attributed(profile_fixture)
    -> None
"""
import pytest
from django.contrib.auth.models import User
from django.db import IntegrityError

from profiles.models import Profile


@pytest.mark.django_db
def test_profile_str(profile_fixture):
    """
    Test if the Profile.__str__() method works as expected.

        Parameters:
            profile_fixture (Profile): A Profile instance.

        Returns:
            None
    """
    profile = Profile.objects.get(id=1)
    user = User.objects.get(id=1)
    assert str(profile) == f"{user.username}"


@pytest.mark.django_db
def test_profile_create_fail_user_already_attributed(profile_fixture):
    """
    Test if creating a Profile with a user that is already linked
    to another Profile throw an Error.

        Parameters:
            profile_fixture (Profile): A Profile instance.

        Returns:
            None
    """
    data = {
        "user": profile_fixture.user,
        "favorite_city": "dummy2",
    }
    with pytest.raises(IntegrityError,
                       match="UNIQUE constraint failed: "
                             "profiles_profile.user_id"):
        Profile.objects.create(**data)
