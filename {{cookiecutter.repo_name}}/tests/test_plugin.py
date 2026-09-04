from django.apps import apps

from byro.common.utils import get_plugins

APP_LABEL = "{{cookiecutter.module_name}}"


def test_app_config_with_plugin_meta_is_loaded():
    app = apps.get_app_config(APP_LABEL)
    assert type(app).__name__ == "PluginApp"
    assert hasattr(app, "ByroPluginMeta")


def test_plugin_is_listed_by_byro():
    assert APP_LABEL in [app.label for app in get_plugins()]
