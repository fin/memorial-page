from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "mysite"

    def ready(self):
        import_module("mysite.receivers")
