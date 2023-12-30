# -*- coding: utf-8 -*-

from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    label = 'users'
    verbose_name = 'Пользователи'

    def ready(self):
        import users.signals.profile_signal
