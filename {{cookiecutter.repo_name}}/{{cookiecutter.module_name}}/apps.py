from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

from . import __version__


class PluginApp(AppConfig):
    name = "{{cookiecutter.module_name}}"
    verbose_name = _("{{cookiecutter.human_name}}")

    class ByroPluginMeta:
        name = _("{{cookiecutter.human_name}}")
        author = "{{cookiecutter.author_name}}"
        description = _("{{cookiecutter.short_description}}")
        visible = True
        version = __version__

    def ready(self):
        from . import signals  # noqa
