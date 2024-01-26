# -*- coding: utf-8 -*-

from django.contrib import admin
from django import forms

from practics.models import (Practicum, Screens,
                             ScreenTextBlock, ScreenImageBlock,
                             ScreenPopupBlock, ScreenButton)
from nested_admin import (NestedModelAdmin,
                          NestedStackedInline,
                          NestedTabularInline)


class ScreenButtonInline(NestedStackedInline):
    model = ScreenButton
    fields= ['screen', 'button_title']
    extra = 0


class ScreenTextBlockInline(NestedStackedInline):
    model = ScreenTextBlock
    extra = 0


class ScreenImageBlockInline(NestedStackedInline):
    model = ScreenImageBlock
    extra = 0


class ScreenPopupBlockInline(NestedStackedInline):
    model = ScreenPopupBlock
    extra = 0


class ScreensInline(NestedStackedInline):
    model = Screens
    inlines = [ScreenTextBlockInline,
               ScreenImageBlockInline,
               ScreenPopupBlockInline,
               ScreenButtonInline]
    extra = 1


@admin.register(Practicum)
class PracticumAdmin(NestedModelAdmin):
    inlines = [ScreensInline]
