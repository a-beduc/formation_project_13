Installation
============

.. _install-from-repository:

From repository
---------------

Using Pip
^^^^^^^^^

#. Open the terminal.
#. Navigate to the desired empty directory.
#. Clone the GitHub repository:

    .. code-block:: console

        $ git clone https://github.com/a-beduc/formation_project_13.git
        $ cd formation_project_13

#. create a virtual environment:

    .. code-block:: console

       $ python -m venv .venv

#. activate the virtual environment:

    Linux / MacOS,

    .. code-block:: console

       $ source .venv/bin/activate

    or Windows.

    .. code-block:: console

       $ .venv\Scripts\activate

#. Install dependencies:

    Only necessary,

    .. code-block:: console

       $ pip install -r requirements.txt

    or with dev tools.

    .. code-block:: console

       $ pip install -r requirements.dev.txt

Using Uv
^^^^^^^^

Step 1-3 are similar than with pip.

#. Open the terminal.
#. Navigate to the desired empty directory.
#. Clone the GitHub repository:

    .. code-block:: console

       $ git clone https://github.com/a-beduc/formation_project_13.git
       $ cd formation_project_13

#. Install **uv**, guide: https://docs.astral.sh/uv/getting-started/installation/
#. Install dependencies

    Only necessary,

    .. code-block:: console

       $ uv sync --no-dev

    or with dev tools.

    .. code-block:: console

       $ uv sync


.. _install-from-image:

From image
----------

With embedded demo database
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Copy the file **docker-compose.demo.yaml** from the repository: https://github.com/a-beduc/formation_project_13
#. Install **Docker Desktop** according to your OS: https://docs.docker.com/get-started/get-docker/

With clean database and volume
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first run should populate the volume with a database containing only a superuser.

#. Copy the file **docker-compose.yaml** from the repository: https://github.com/a-beduc/formation_project_13
#. Install **Docker Desktop** according to your OS: https://docs.docker.com/get-started/get-docker/
#. Verify that docker is running.
#. Create a new empty volume named **empty-volume**:

    .. code-block::

       $ docker volume create empty-volume
