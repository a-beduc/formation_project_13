"""
Django tests for the 'oc_lettings_site/views.py' file.

Functions:
    test_index_views() -> None
"""
import pytest
from django.test import Client
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
    path = reverse('index')
    response = client.get(path)
    assert response.status_code == 200
    assertTemplateUsed(response, 'index.html')
