{{cookiecutter.human_name}}
{{ "=" * cookiecutter.human_name|length }}

This is a plugin for `byro`_. {{cookiecutter.short_description}}

Requirements
------------

- Python 3.12 or newer
- A `byro`_ installation (Django 5.2)

Development setup
-----------------

1. Make sure that you have a working `byro development setup`_.

2. Clone this repository, e.g. into byro's ``src/local/`` directory.

3. Activate the virtual environment you use for byro development and install
   the plugin in editable mode::

       $ pip install -e ".[dev]"

   Alternatively, run ``./install_local_plugins.sh`` from byro's ``src/``
   directory to install every plugin found in ``src/local/``.

4. Restart your local byro server. The plugin is registered through the
   ``byro.plugin`` entry point and shows up under *Settings → About*.

Tests and code style
--------------------

Run the test suite against byro's test settings with an SQLite database::

    $ BYRO_DB_ENGINE=sqlite3 pytest

Format and lint the code the same way the byro core does::

    $ isort .
    $ black .
    $ flake8 .

Translations
------------

Create or update the German message catalogue from within the plugin package::

    $ cd {{cookiecutter.module_name}}
    $ django-admin makemessages -l de

Compile the catalogues from the repository root (this also happens
automatically when the package is built in an environment where Django is
installed, e.g. via ``install_local_plugins.sh``)::

    $ django-admin compilemessages

Plugin structure
----------------

- ``{{cookiecutter.module_name}}/apps.py`` holds the ``AppConfig`` with the
  ``ByroPluginMeta`` metadata that byro reads. Django only discovers it from
  ``apps.py``, so keep it there.
- ``{{cookiecutter.module_name}}/signals.py`` is imported from ``ready()``;
  connect your signal receivers there.
- A ``urls.py`` next to it is picked up automatically and mounted under the
  URL namespace ``plugins:{{cookiecutter.module_name}}:``.
- The ``byro.plugin`` entry point in ``pyproject.toml`` points at the package
  itself; byro only uses the module name to add the app to ``INSTALLED_APPS``.

See the `byro plugin documentation`_ for the available signals and hooks.

License
-------

Copyright {{cookiecutter.year}} {{cookiecutter.author_name}}

Released under the terms of the Apache License 2.0


.. _byro: https://github.com/byro/byro
.. _byro development setup: https://byro.readthedocs.io/en/latest/developer/setup.html
.. _byro plugin documentation: https://byro.readthedocs.io/en/latest/developer/plugins/
