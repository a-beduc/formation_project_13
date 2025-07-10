"""
Django views for the 'oc_lettings_site' app.

Functions:
    index(request) -> HttpResponse
    custom_page_not_found_view(request, exception) -> HttpResponse
    custom_error_view(request) -> HttpResponse
"""
import logging

from django.http import Http404
from django.shortcuts import render
from sentry_sdk import capture_message


logger = logging.getLogger(__name__)


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque
# molestie quam lobortis leo consectetur ullamcorper non id est.
# Praesent dictum, nulla eget feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum,
# eget consequat ipsum lobortis quis. Phasellus eleifend ex auctor
# venenatis tempus. Aliquam vitae erat ac orci placerat luctus. Nullam
# elementum urna nisi, pellentesque iaculis enim cursus in. Praesent
# volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    """
    Return the HttpResponse corresponding to the basic endpoint.

        Parameters:
            request (django.http.HttpRequest): The request object.

        Returns:
            response (django.http.HttpResponse): The HttpResponse.
    """
    return render(request, 'index.html')


def custom_page_not_found_view(request, exception):
    capture_message(f"404 on {request.path}", level="warning")
    logger.warning(f"404:{request.path}", exc_info=exception)
    return render(request, "errors/404.html", status=404)


def custom_error_view(request):
    logger.error(f"500 on {request.path}")
    return render(request, "errors/500.html", status=500)

