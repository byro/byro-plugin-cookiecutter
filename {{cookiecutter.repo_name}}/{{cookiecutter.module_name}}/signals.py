"""Signal receivers for {{cookiecutter.human_name}}.

byro talks to plugins through Django signals. This module is imported from
``PluginApp.ready()`` in ``apps.py``, so connect your receivers here.

All available signals are documented at
https://byro.readthedocs.io/en/latest/developer/plugins/general.html
"""

# Example: add an entry to the byro sidebar.
#
# ``nav_event`` sends the current request as ``sender`` and expects a dict
# with at least ``label`` and ``url``. ``icon`` is a ForkAwesome icon name and
# ``active`` marks the entry for the current page. Views of this plugin live in
# the URL namespace ``plugins:{{cookiecutter.module_name}}:`` as soon as a
# ``urls.py`` exists next to this file.
#
# from django.dispatch import receiver
# from django.urls import reverse
# from django.utils.translation import gettext_lazy as _
#
# from byro.office.signals import nav_event
#
#
# @receiver(nav_event)
# def sidebar_entry(sender, **kwargs):
#     request = sender
#     return {
#         "icon": "puzzle-piece",
#         "label": _("{{cookiecutter.human_name}}"),
#         "url": reverse("plugins:{{cookiecutter.module_name}}:index"),
#         "active": bool(
#             request.resolver_match
#             and request.resolver_match.namespace
#             == "plugins:{{cookiecutter.module_name}}"
#         ),
#     }
