Getting started
===============

Before starting the application, make sure all prerequisites are met and environment variables are correctly configured.
Without this configuration, the project will not run properly.

Prerequisites
-------------

Secret Key
^^^^^^^^^^

Django requires a secret key. If you don't have one, you can generate a new one: `Secret Key <URL_SECRET_KEY_>`_.

.. _URL_SECRET_KEY: https://djecrety.ir/

Sentry
^^^^^^

The project uses `Sentry <URL_SENTRY_>`_ for exception and error tracking.

#. If you have not already created an account, go to: `Getting started with sentry <URL_SENTRY_GETTING_STARTED_>`_.
#. Create a new Django project and follow instruction to configure it.
#. Copy the provided DSN.
#. You can find the DSN in your project settings under **Project > Client Key**.

.. _URL_SENTRY: https://sentry.io/welcome/
.. _URL_SENTRY_GETTING_STARTED: https://sentry.io/signup/

Environment variables
---------------------

To run, the project must find the following environment variables:

* DJANGO_SECRET_KEY: Django signing key.
* DJANGO_ALLOWED_HOSTS: Server addresses.
* DEBUG: For debug mode, default is production mode. Activate with "True".
* DJANGO_SENTRY_DSN: DSN provided by Sentry.

Running the application
-----------------------

From repository
^^^^^^^^^^^^^^^

You must have completed the steps found in :ref:`install-from-repository`.

#. Open a terminal where your project is located (make sure your virtual environment is activated).
#. Create an `.env` file containing the required environment variables, you can copy and modify `.env.example`.
#. If you run the application with ``DEBUG=False``, collect the statics:

    .. code-block:: console

        $ python manage.py collectstatic

#. Start the application

    .. code-block:: console

        $ python mangage.py runserver

From Docker image
^^^^^^^^^^^^^^^^^

You must have completed the steps found in :ref:`install-from-image`.

#. Create an `.env` file containing the required environment variables, you can copy and modify `.env.example`.
#. Make sure Docker is running.
#. Run the container:

    With embedded database:

    .. code-block:: console

        $ docker compose -f docker-compose.demo.yaml up

    With volume:

    .. code-block:: console

        $ docker compose -f docker-compose.yaml up

The project will be accessible at: http://localhost:8000/
