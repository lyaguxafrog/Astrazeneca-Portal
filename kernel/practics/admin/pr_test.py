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
    inlines = [ButtonsInline]
