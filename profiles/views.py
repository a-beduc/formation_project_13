"""
Django views for the 'profiles' app.

Functions:
    index(request) -> HttpResponse
    letting(request) -> HttpResponse
"""
from django.shortcuts import render, get_object_or_404

from profiles.models import Profile


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex,
# sed consequat libero pulvinar eget. Fusc faucibus, urna quis auctor
# pharetra, massa dolor cursus neque, quis dictum lacus d
def index(request):
    """
    Return the HttpResponse corresponding to the profiles/
    endpoint.

        Parameters:
            request (django.http.HttpRequest): The request object.

        Returns:
            response (django.http.HttpResponse): The HttpResponse.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac laoreet
# neque quis, pellentesque dui. Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue. Pellentesque habitant morbi
# tristique senectus et netus et males
def profile(request, username):
    """
    Return the HttpResponse corresponding to the profiles/<username>/
    endpoint.

        Parameters:
            request (django.http.HttpRequest): The request object.
            username (str): The profile username.

        Returns:
            response (django.http.HttpResponse): The HttpResponse.
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
