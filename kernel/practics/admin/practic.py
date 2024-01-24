# -*- coding: utf-8 -*-

from django.contrib import admin

from practics.models import Practicum

@admin.register(Practicum)
class PracticumAdmin(admin.ModelAdmin):
    model = Practicum
