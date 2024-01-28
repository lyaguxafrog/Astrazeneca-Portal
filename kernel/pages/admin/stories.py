# -*- coding: utf-8 -*-

from django.contrib import admin
from pages.models import Story
from config.admin import custom_admin_site

admin.site = custom_admin_site


class StoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_active'
    )
    fields = (

        'title',
        'content',
        'avatar',
        'cover_image',
        'video',
        # 'color',
        'link_to_page',
        'specialties',
        'is_active'
    )


admin.site.register(Story, StoryAdmin)
