# -*- coding: utf-8 -*-

from django.contrib import admin

from practics.models import (Practicum, Screens,
                             ScreenTextBlock, ScreenImageBlock,
                             ScreenPopupBlock, ScreenButton)
from nested_admin import (NestedModelAdmin,
                          NestedStackedInline,
                          NestedTabularInline)


class ScreenButtonInline(NestedStackedInline):
    model = ScreenButton
    extra = 0
    exclude = ['screen_redirect',]
    fk_name = 'screen'

class ScreenTextBlockInline(NestedStackedInline):
    model = ScreenTextBlock
    extra = 0


class ScreenImageBlockInline(NestedStackedInline):
    model = ScreenImageBlock
    fields = ['image', 'order']
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
    extra = 0


@admin.register(Practicum)
class PracticumAdmin(NestedModelAdmin):
    inlines = [ScreensInline]
    exclude = [
        'image_desktop_810px',
        'image_desktop_1620px',
        'image_mobile_400px',
        'image_mobile_800px']

    search_fields = ['title', 'desription', 'pacient_description']
