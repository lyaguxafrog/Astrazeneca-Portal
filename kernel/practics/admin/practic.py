# -*- coding: utf-8 -*-

from django.contrib import admin
from config.admin import custom_admin_site

admin.site = custom_admin_site

from practics.models import (Practicum, Screens,
                             ScreenTextBlock_left, ScreenImageBlock_left,
                             ScreenPopupBlock_left, ScreenButton_left,
                             ScreenTextBlock_right, ScreenPopupBlock_right,
                             ScreenButton_right, ScreenImageBlock_right)
from nested_admin import (NestedModelAdmin,
                          NestedStackedInline,
                          NestedTabularInline)

# лево
class ScreenButtonInline_left(NestedStackedInline):
    model = ScreenButton_left
    extra = 0
    exclude = ['screen_redirect',]
    fk_name = 'screen'

class ScreenTextBlockInline_left(NestedStackedInline):
    model = ScreenTextBlock_left
    extra = 0


class ScreenImageBlockInline_left(NestedStackedInline):
    model = ScreenImageBlock_left
    fields = ['image', 'order']
    extra = 0


class ScreenPopupBlockInline_left(NestedStackedInline):
    model = ScreenPopupBlock_left
    extra = 0

# право

class ScreenButtonInline_right(NestedStackedInline):
    model = ScreenButton_right
    extra = 0
    exclude = ['screen_redirect',]
    fk_name = 'screen'

class ScreenTextBlockInline_right(NestedStackedInline):
    model = ScreenTextBlock_right
    extra = 0


class ScreenImageBlockInline_right(NestedStackedInline):
    model = ScreenImageBlock_right
    fields = ['image', 'order']
    extra = 0


class ScreenPopupBlockInline_right(NestedStackedInline):
    model = ScreenPopupBlock_right
    extra = 0

class ScreensInline(NestedStackedInline):
    model = Screens
    inlines = [ScreenTextBlockInline_left,
               ScreenImageBlockInline_left,
               ScreenPopupBlockInline_left,
               ScreenButtonInline_left,
               ScreenTextBlockInline_right,
               ScreenImageBlockInline_right,
               ScreenPopupBlockInline_right,
               ScreenButtonInline_right,]
    extra = 0


class PracticumAdmin(NestedModelAdmin):
    inlines = [ScreensInline]
    exclude = [
        'image_desktop_810px',
        'image_desktop_1620px',
        'image_mobile_400px',
        'image_mobile_800px']

    search_fields = ['title', 'desription', 'pacient_description']


admin.site.register(Practicum, PracticumAdmin)
