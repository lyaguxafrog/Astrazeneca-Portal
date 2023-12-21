# -*- coding: utf-8 -*-

from django.contrib import admin
from pages.models import Drug


@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'brief_info'
    )
