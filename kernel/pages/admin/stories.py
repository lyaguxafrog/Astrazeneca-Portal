# -*- coding: utf-8 -*-

from django.contrib import admin
from pages.models import Story

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_active'
    )
