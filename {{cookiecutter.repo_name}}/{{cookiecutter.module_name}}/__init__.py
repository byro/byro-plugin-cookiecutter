from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PluginApp(AppConfig):
    name = '{{cookiecutter.module_name}}'
    verbose_name = _('{{cookiecutter.human_name}}')

    class ByroPluginMeta:
        name = _('{{cookiecutter.human_name}}')
        author = '{{cookiecutter.author_name}}'
        description = _('{{cookiecutter.short_description}}')
        visible = True
        version = '0.0.1'

    def ready(self):
        from . import signals  # NOQA


default_app_config = '{{cookiecutter.module_name}}.PluginApp'
