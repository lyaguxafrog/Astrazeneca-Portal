# -*- coding: utf-8 -*-

from django.contrib import admin
from config.admin import custom_admin_site

admin.site = custom_admin_site

from practics.models import (Practicum, Screens, ScreenTextBlock_right,
                             ScreenButton_left, ScreenButton_right,
                             ScreenImageBlock_left, ScreenImageBlock_right,
                             ScreenPopupBlock_left, ScreenPopupBlock_right,
                             ScreenTextBlock_left, PopUpPoint_left, PopUpPoint_right)

from nested_admin import (NestedModelAdmin,
                          NestedStackedInline,
                          NestedTabularInline)

from polymorphic.admin import PolymorphicInlineSupportMixin, StackedPolymorphicInline


class PopUpPointleftInline(admin.StackedInline):
    model = PopUpPoint_left

class PopUpPointrightInline(admin.StackedInline):
    model = PopUpPoint_right

class ScreensInline(StackedPolymorphicInline):

    class ScreenTextBlockleftInline(StackedPolymorphicInline.Child):
        model = ScreenTextBlock_left

    class ScreenImageBlockleftInline(StackedPolymorphicInline.Child):
        model = ScreenImageBlock_left

    class ScreenPopupBlockleftInline(StackedPolymorphicInline.Child):
        model = ScreenPopupBlock_left
        inlines = (PopUpPointleftInline,)

    class ScreenButtonleftInline(StackedPolymorphicInline.Child):
        model = ScreenButton_left


    # право
    class ScreenTextBlockrightInline(StackedPolymorphicInline.Child):
        model = ScreenTextBlock_right

    class ScreenImageBlockrightInline(StackedPolymorphicInline.Child):
        model = ScreenImageBlock_right

    class ScreenPopupBlockrightInline(StackedPolymorphicInline.Child):
        model = ScreenPopupBlock_right
        inlines = (PopUpPointrightInline,)

    class ScreenButtonrightInline(StackedPolymorphicInline.Child):
        model = ScreenButton_right

    model = Screens
    child_inlines = (
        ScreenTextBlockleftInline,
        ScreenImageBlockleftInline,
        ScreenPopupBlockleftInline,
        ScreenButtonleftInline,
        ScreenTextBlockrightInline,
        ScreenImageBlockrightInline,
        ScreenPopupBlockrightInline,
        ScreenButtonrightInline,
    )


class PracticumAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):
    inlines = (ScreensInline,)
    exclude = [
        'image_desktop_810px',
        'image_desktop_1620px',
        'image_mobile_400px',
        'image_mobile_800px']

    search_fields = ['title', 'desription', 'pacient_description']


admin.site.register(Practicum, PracticumAdmin)
