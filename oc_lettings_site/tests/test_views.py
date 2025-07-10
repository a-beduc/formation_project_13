"""
Django tests for the 'oc_lettings_site/views.py' file.

Functions:
    test_index_views() -> None
    disable_sentry_logging() -> None
    test_custom_404_views(disable_sentry_logging) -> None
"""
import pytest
import sentry_sdk
from django.test import Client, override_settings
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_index_views():
    """
    Test if the index view is working as expected. Using the proper url
    and template.

        Returns:
            None
    """
    client = Client()
    index_path = reverse('index')
    response = client.get(index_path)
    assert response.status_code == 200
    assertTemplateUsed(response, 'index.html')


@pytest.fixture
def disable_sentry_logging():
    """
    Fixture to block the loggings from being sent to sentry.

        Returns:
            None
    """
    sentry_sdk.init(dsn="")


@override_settings(DEBUG=False)
def test_custom_404_views(disable_sentry_logging):
    """
    Test that a 404 error use the right template in a prod environment.

        Returns:
            None
    """
    client = Client()
    response = client.get('unknown_page')
    assert response.status_code == 404
    assertTemplateUsed(response, 'errors/404.html')
