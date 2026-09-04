byro-plugin-cookiecutter
========================

A `cookiecutter`_ template to bootstrap a `byro`_ plugin that matches the
current byro core (Python 3.12 or newer, Django 5.2).

Usage
-----

Let's pretend you want to create a byro plugin called "superplugin".
Install ``cookiecutter`` (for example with ``pipx install cookiecutter`` or
``uv tool install cookiecutter``) and run it in the directory where the new
project folder should be created::

    $ cd <your-project-folder-parent>
    $ cookiecutter gh:byro/byro-plugin-cookiecutter

Answer some questions, and once you're done, you'll find yourself with
a project directory just ready for you::

    repo_name [byro-superplugin]: byro-superplugin
    repo_url [https://github.com/yourname/byro-superplugin]: https://github.com/myuser/byro-superplugin
    module_name [byro_superplugin]:
    human_name [The byro super plugin]: Super Plugin
    author_name [Your name]: J Random Developer
    author_email [you@example.org]: jrandom@example.org
    year [2026]:
    short_description [Short description]: The best plugin

``module_name`` is derived from ``repo_name`` and ``year`` defaults to the
current year, so both can usually be accepted as they are.

Now, change to the newly created directory::

    $ cd byro-superplugin

Voila, there's your plugin structure!

What you get
------------

::

    byro-superplugin/
    ├── pyproject.toml          metadata, byro.plugin entry point, isort/pytest config
    ├── setup.py                build hook that compiles translations
    ├── .flake8                 flake8 rules matching the byro core
    ├── .github/                CI workflow (isort, black, flake8, pytest), dependabot
    ├── tests/test_plugin.py    smoke test: byro loads the plugin
    └── byro_superplugin/
        ├── __init__.py         __version__
        ├── apps.py             AppConfig with ByroPluginMeta
        ├── signals.py          signal receivers, imported from ready()
        ├── locale/de/          German message catalogue
        ├── static/             static files
        └── templates/          templates

Next steps
----------

Install the plugin into your byro development environment with
``pip install -e ".[dev]"``, or clone it into byro's ``src/local/`` and run
``./install_local_plugins.sh``. Restart byro and check *Settings → About*.

Please refer to the `byro developer documentation`_ to see what you can do with
byro.

If your project is hosted on GitHub, please add the ``byro-plugin`` topic, to
help others see what byro is used for.

.. _byro: https://github.com/byro/byro
.. _cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _byro developer documentation: https://byro.readthedocs.io/en/latest/developer/plugins/
