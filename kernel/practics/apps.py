# -*- coding: utf-8 -*-

from django.apps import AppConfig

class PracticsConfig(AppConfig):
    name = 'practics'
    label = 'practics'
    verbose_name = 'Практикумы'

    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        import practics.signals
