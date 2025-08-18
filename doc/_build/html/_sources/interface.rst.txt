Programming interfaces
======================

OC Lettings is built upon classic Django views.

Organisation
------------

The project is made of the following modules :

+ ``oc_lettings_site``: Contains the global routes, the views for the homepage and the custom errors handlers. It contains the ``settings.py`` file.
+ ``profiles``: Contains the routes and the views for profile ressources.
+ ``lettings``: Contains the routes and the views for letting ressources.

Routes
------

+----------------------+----------------------------------+---------------------------------------------+
| URL                  | View                             | Description                                 |
+======================+==================================+=============================================+
| ``/``                | ``oc_lettings_site.views.index`` | Homepage with links to Lettings & Profiles. |
+----------------------+----------------------------------+---------------------------------------------+
| ``/profiles/``       | ``profiles.views.index``         | Lists all user profiles.                    |
+----------------------+----------------------------------+---------------------------------------------+
| ``/profiles/<user>/``| ``profiles.views.profile``       | Displays details of a specific profile.     |
+----------------------+----------------------------------+---------------------------------------------+
| ``/lettings/``       | ``lettings.views.index``         | Lists all available lettings.               |
+----------------------+----------------------------------+---------------------------------------------+
| ``/lettings/<id>/``  | ``lettings.views.letting``       | Displays details of a specific letting.     |
+----------------------+----------------------------------+---------------------------------------------+

Error handling
--------------

The following errors are handled to ensure that the user experience is consistent in case of an error.

+ **404 - Page not found**: handled by ``oc_lettings_site.views.custom_page_not_found_view``.
+ **500 - Internal server error**: handled by ``oc_lettings_site.views.custom_error_view``.
