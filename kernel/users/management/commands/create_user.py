#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from decouple import config


class Command(BaseCommand):
    help = 'Create a default admin user if it does not exist.'

    def handle(self, *args, **options):
        username = 'admin'
        email = 'admin@admin.com'
        password = config("ADMIN_PASSWORD")


        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f'Successfully created admin user: {username}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Admin user already exists: {username}'))
