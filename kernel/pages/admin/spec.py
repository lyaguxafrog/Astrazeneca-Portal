# -*- coding: utf-8 -*-

from django.contrib import admin
from pages.models import Specialty




@admin.register(Specialty)
class SpecAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
    )
