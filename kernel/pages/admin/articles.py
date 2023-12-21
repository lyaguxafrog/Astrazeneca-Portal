# -*- coding: utf-8 -*-

from django.contrib import admin
from pages.models import Articles

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = (
        "article_name",
        "article_type"
    )
