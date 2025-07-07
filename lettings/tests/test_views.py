"""
Django tests for the 'lettings/views.py' file.

Functions:
    test_index_views() -> None
    test_letting_views(letting_fixture) -> None
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
    path = reverse('lettings:index')
    response = client.get(path)
    assert response.status_code == 200
    assertTemplateUsed(response, 'lettings/index.html')


@pytest.mark.django_db
def test_letting_views(letting_fixture):
    """
    Test if the index view is working as expected. Using the proper url
    and template and displaying the expected data.

        Parameters:
            letting_fixture (Letting): A Letting instance.

        Returns:
            None
    """
    client = Client()
    path = reverse('lettings:letting',
                   kwargs={"letting_id": letting_fixture.id})
    response = client.get(path)
    assert response.status_code == 200
    assertTemplateUsed(response, 'lettings/letting.html')

    content = response.content.decode('utf-8')
    assert f"{letting_fixture.address.number}" in content
    assert f"{letting_fixture.address.street}" in content
    assert f"{letting_fixture.address.city}" in content
    assert f"{letting_fixture.address.state}" in content
    assert f"{letting_fixture.address.zip_code}" in content
    assert f"{letting_fixture.address.country_iso_code}" in content
