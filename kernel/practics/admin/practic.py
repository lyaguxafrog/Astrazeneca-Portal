# -*- coding: utf-8 -*-

from django.contrib import admin
from config.admin import custom_admin_site
from practics.models import (Practicum, Screens, ScreenTextBlock_left,
                             ScreenTextBlock_right, ScreenImageBlock_left,
                             ScreenImageBlock_right, ScreenPopupBlock_left,
                             ScreenPopupBlock_right, ScreenButton_left,
                             ScreenButton_right)

from polymorphic.admin import PolymorphicInlineSupportMixin, PolymorphicParentModelAdmin, PolymorphicInlineModelAdmin, StackedPolymorphicInline

admin.site = custom_admin_site



class ScreenAdmin(StackedPolymorphicInline):

    class TextBlock_left(StackedPolymorphicInline.Child):
        model = ScreenTextBlock_left

    model = Screens
    child_inlines = {
        TextBlock_left
    }

class PracticumAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):
    inlines = (ScreenAdmin,)


admin.site.register(Practicum, PracticumAdmin)
