# -*- coding: utf-8 -*-

from django.contrib import admin
from pages.models import Specialty
from config.admin import custom_admin_site

admin.site = custom_admin_site


class SpecAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
    )


admin.site.register(Specialty, SpecAdmin)
