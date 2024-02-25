# -*- coding: utf-8 -*-

from django.contrib import admin

from practics.models import PrTest, AnswerButtons
from nested_admin import (NestedModelAdmin, NestedStackedInline)
from config.admin import custom_admin_site

admin.site = custom_admin_site

class ButtonsInline(admin.StackedInline):
    model = AnswerButtons
    extra = 0


class PrTestAdmin(admin.ModelAdmin):
    model = PrTest
    list_display = [
        'title',
    ]
    fields = [
        'title',
        'question',
        'image',
        'approvals_and_decodings',
        'next_test',
        'speciality',
        'priority',
    ]
    inlines = [ButtonsInline]
    search_fields = ['title','question']

admin.site.register(PrTest, PrTestAdmin)
