# -*- coding: utf-8 -*-

from django.contrib import admin
from config.admin import custom_admin_site
from practics.models import (Practicum, Screens, ScreenTextBlock_left,
                             ScreenTextBlock_right, ScreenImageBlock_left,
                             ScreenImageBlock_right, ScreenPopupBlock_left,
                             ScreenPopupBlock_right, ScreenButton_left,
                             ScreenButton_right, ContentBlock)

from polymorphic.admin import (PolymorphicInlineSupportMixin,
                               PolymorphicParentModelAdmin,
                               PolymorphicInlineModelAdmin,
                               StackedPolymorphicInline)

# настройки админки в config/admin.py
admin.site = custom_admin_site


class ContentBlockAdmin(StackedPolymorphicInline):

    class Left_text(StackedPolymorphicInline.Child):
        model = ScreenTextBlock_left


    class Left_image(StackedPolymorphicInline.Child):
        model = ScreenImageBlock_left

    model = ContentBlock
    child_inlines = (
        Left_text,
        Left_image
    )

class ScreenInline(PolymorphicInlineSupportMixin, admin.StackedInline):
    model = Screens
    extra = 0
    inlines = (ContentBlockAdmin, )


class PracticumAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):
    inlines = (ScreenInline, )


admin.site.register(Practicum, PracticumAdmin)
