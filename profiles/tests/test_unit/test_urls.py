"""
Django tests for the 'profiles/urls.py' file.

Functions:
    test_profile_index() -> None
    test_profile_profiles(profile_fixture) -> None
"""
import pytest
from django.urls import reverse, resolve

from profiles.views import index, profile


def test_profile_index():
    """
    Test that the url '/profiles/' is properly resolved.

        Returns:
            None
    """
    path = reverse('profiles:index')
    assert path == "/profiles/"

    match = resolve(path)
    assert match.view_name == "profiles:index"
    assert match.func == index


@pytest.mark.django_db
def test_profile_profile(profile_fixture):
    """
    Test that the url '/profiles/<username>/' is properly resolved.
    Args:
        profile_fixture (Profile): A Profile instance.

    Returns:
        None
    """
    path = reverse('profiles:profile',
                   kwargs={'username': profile_fixture.user.username})
    assert path == f"/profiles/{profile_fixture.user.username}/"

    match = resolve(path)
    assert match.view_name == "profiles:profile"
    assert match.func == profile
