from django.apps import AppConfig
from django.utils.translation import ugettext_lazy


class PluginApp(AppConfig):
    name = '{{cookiecutter.module_name}}'
    verbose_name = '{{cookiecutter.human_name}}'

    class ByroPluginMeta:
        name = ugettext_lazy('{{cookiecutter.human_name}}')
        author = '{{cookiecutter.author_name}}'
        description = ugettext_lazy('{{cookiecutter.short_description}}')
        visible = True
        version = '0.0.1'

    def ready(self):
        from . import signals  # NOQA


default_app_config = '{{cookiecutter.module_name}}.PluginApp'
