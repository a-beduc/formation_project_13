"""
Django tests for the 'lettings/urls.py' file.

Functions:
    test_letting_index() -> None
    test_letting_lettings(letting_fixture) -> None
"""
import pytest
from django.urls import reverse, resolve

from lettings.views import index, letting


def test_letting_index():
    """
    Test that the url '/lettings/' is properly resolved.

        Returns:
            None
    """
    path = reverse('lettings:index')
    assert path == "/lettings/"

    match = resolve(path)
    assert match.view_name == "lettings:index"
    assert match.func == index


@pytest.mark.django_db
def test_letting_letting(letting_fixture):
    """
    Test that the url '/lettings/<letting_id>/' is properly resolved.
    Args:
        letting_fixture (Letting): A Letting instance.

    Returns:
        None
    """
    path = reverse('lettings:letting',
                   kwargs={'letting_id': letting_fixture.id})
    assert path == f"/lettings/{letting_fixture.id}/"

    match = resolve(path)
    assert match.view_name == "lettings:letting"
    assert match.func == letting
