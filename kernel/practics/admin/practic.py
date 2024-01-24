# -*- coding: utf-8 -*-

from django.contrib import admin
from practics.models import (Practicum, Screens,
                             ScreenTextBlock, ScreenImageBlock,
                             ScreenPopupBlock)
from nested_admin import (NestedModelAdmin, NestedInlineModelAdmin,
                          NestedStackedInline, NestedTabularInline)

class ScreenTextBlockInline(NestedTabularInline):
    model = ScreenTextBlock
    extra = 0


class ScreenImageBlockInline(NestedTabularInline):
    model = ScreenImageBlock
    extra = 0


class ScreenPopupBlockInline(NestedTabularInline):
    model = ScreenPopupBlock
    extra = 0

class ScreensInline(NestedStackedInline):
    model = Screens
    inlines = [ScreenTextBlockInline,
               ScreenImageBlockInline,
               ScreenPopupBlockInline]
    extra = 1

@admin.register(Practicum)
class PracticumAdmin(NestedModelAdmin):
    inlines = [ScreensInline]
