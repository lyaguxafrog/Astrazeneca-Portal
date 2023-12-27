# -*- coding: utf-8 -*-

from django.apps import AppConfig


class PagesConfig(AppConfig):
    name = 'pages'
    label = 'pages'
    verbose_name = 'Контент'

    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        import pages.signals
