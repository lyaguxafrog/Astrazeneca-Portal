# -*- coding: utf-8 -*-

from django.contrib import admin

from practics.models import PrTest

@admin.register(PrTest)
class PrTestAdmin(admin.ModelAdmin):
    model = PrTest
