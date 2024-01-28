# -*- coding: utf-8 -*-

from django.contrib import admin
from pages.models import Events
from config.admin import custom_admin_site

admin.site = custom_admin_site

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


admin.site.register(Events, EventsAdmin)
