# -*- coding: utf-8 -*-

from django.contrib import admin
from config.admin import custom_admin_site

admin.site = custom_admin_site

from practics.models import Practicum, Screens
