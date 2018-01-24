byro-plugin-cookiecutter
========================

A simple `cookiecutter`_ template to bootstrap a `byro`_ plugin.

Usage
-----

Let's pretend you want to create a byro plugin called "superplugin". 
First, create a virtual Python 3.6 environment and install the
``cookiecutter`` package using pip. Next, use it to bootstrap your
project folder::

    $ cd <your-project-folder-parent>
    $ cookiecutter https://github.com/byro/byro-plugin-cookiecutter
    
Answer some questions, and once you're done, you'll find yourself with
a project directory just ready for you.

    repo_name [byro-superplugin]: byro-superplugin
    repo_url [GitHub repository URL]: https://github.com/myuser/byro-superplugin
    module_name [byro_superplugin]: byro_superplugin
    human_name [The byro super plugin]: Super Plugin
    author_name [Your name]: J Random Developer
    author_email [Your email]: jrandom@example.org
    year [Current year]: 2017
    short_description [Short description]: The best plugin

Now, change to the newly created directory::

    $ cd byro-superplugin

Voila, there's your plugin structure!

.. _byro: https://github.com/byro/byro
.. _cookiecutter: https://github.com/audreyr/cookiecutter
