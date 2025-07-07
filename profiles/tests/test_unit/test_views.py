"""
Django tests for the 'profiles/views.py' file.

Functions:
    test_index_views() -> None
    test_profile_views(profile_fixture) -> None
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
    path = reverse('profiles:index')
    response = client.get(path)
    assert response.status_code == 200
    assertTemplateUsed(response, 'profiles/index.html')


@pytest.mark.django_db
def test_profile_views(profile_fixture):
    """
    Test if the index view is working as expected. Using the proper url
    and template and displaying the expected data.

        Parameters:
            profile_fixture (Profile): A Profile instance.

        Returns:
            None
    """
    client = Client()
    path = reverse('profiles:profile',
                   kwargs={"username": profile_fixture.user.username})
    response = client.get(path)
    assert response.status_code == 200
    assertTemplateUsed(response, 'profiles/profile.html')

    content = response.content.decode('utf-8')
    assert f"{profile_fixture.user.first_name}" in content
    assert f"{profile_fixture.user.last_name}" in content
    assert f"{profile_fixture.user.email}" in content
    assert f"{profile_fixture.favorite_city}" in content
