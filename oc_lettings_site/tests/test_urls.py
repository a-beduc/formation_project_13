"""
Django tests for the 'oc_lettings_site/urls.py' file.

Functions:
    test_oc_lettings_site_index() -> None
    test_oc_lettings_site_admin() -> None
    test_oc_lettings_site_include_lettings() -> None
    test_oc_lettings_site_include_profiles() -> None
"""
# from django.contrib import admin
from django.urls import reverse, resolve

from lettings.views import index as lettings_index
from oc_lettings_site.views import index as main_index
from profiles.views import index as profiles_index


def test_oc_lettings_site_index():
    """
    Test that the url '/' is properly resolved.

    Returns:
        None
    """
    path = reverse('index')
    assert path == "/"

    match = resolve(path)
    assert match.view_name == "index"
    assert match.func == main_index


def test_oc_lettings_site_include_lettings():
    """
    Test that the url '/lettings/' is properly resolved.

    Returns:
        None
    """
    path = reverse("lettings:index")
    assert path == "/lettings/"

    match = resolve(path)
    assert match.view_name == "lettings:index"
    assert match.func == lettings_index


def test_oc_lettings_site_include_profiles():
    """
    Test that the url '/profiles/' is properly resolved.

    Returns:
        None
    """
    path = reverse("profiles:index")
    assert path == "/profiles/"

    match = resolve(path)
    assert match.view_name == "profiles:index"
    assert match.func == profiles_index
