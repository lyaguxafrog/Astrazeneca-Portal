# -*- coding: utf-8 -*-

from django.contrib import admin
from config.admin import custom_admin_site
from practics.models import (Practicum, Screens, ScreenTextBlock_left,
                             ScreenTextBlock_right, ScreenImageBlock_left,
                             ScreenImageBlock_right, ScreenPopupBlock_left,
                             ScreenPopupBlock_right, ScreenButton_left,
                             ScreenButton_right, ContentBlock, ScreenOption)

from polymorphic.admin import (PolymorphicInlineSupportMixin,
                               PolymorphicParentModelAdmin,
                               PolymorphicInlineModelAdmin,
                               StackedPolymorphicInline,
                               GenericPolymorphicInlineModelAdmin)

# настройки админки в config/admin.py
admin.site = custom_admin_site


class ScreenOptionAdmin(StackedPolymorphicInline):
    model = ScreenOption

    class ScreensInline(StackedPolymorphicInline.Child):
        model = Screens


        class ContentBlockAdmin(StackedPolymorphicInline.Child):

            class Left_text(StackedPolymorphicInline.Child):
                model = ScreenTextBlock_left


            class Left_image(StackedPolymorphicInline.Child):
                model = ScreenImageBlock_left

            model = ContentBlock
            child_inlines = (
                Left_text,
                Left_image
            )

            child_inlines = (
                Left_text,
            )


    child_inlines = (
        ScreensInline,
    )


class PracticumAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):
    inlines = (ScreenOptionAdmin, )


admin.site.register(Practicum, PracticumAdmin)
