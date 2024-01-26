# -*- coding: utf-8 -*-

from django.contrib import admin

from practics.models import PrTest, AnswerButtons
from nested_admin import (NestedModelAdmin, NestedStackedInline)

class ButtonsInline(NestedStackedInline):
    model = AnswerButtons
    extra = 1

@admin.register(PrTest)
class PrTestAdmin(NestedModelAdmin):
    model = PrTest
    list_display = [
        'title',
    ]
    fields = [
        'title',
        'question',
        'image',
        'approvals_and_decodings',
        'speciality',
        'priority',
    ]
    inlines = [ButtonsInline]
    search_fields = ['title','question']
