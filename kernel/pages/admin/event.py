# -*- coding: utf-8 -*-

from django.contrib import admin
from pages.models import Events


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date'
    )
    fields = (
        'name',
        'date',
        'cover',
        'text',
        'url'
    )
