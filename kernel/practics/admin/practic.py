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
                               StackedPolymorphicInline,
                               GenericPolymorphicInlineModelAdmin)

# настройки админки в config/admin.py
admin.site = custom_admin_site


class inline1(admin.StackedInline):
    model = ScreenTextBlock_left

class inline2(admin.StackedInline):
    model = ScreenButton_right

class ScreenAdmin(admin.ModelAdmin):
    inlines = [inline1, inline2]
    raw_id_fields = ('related_model',)


admin.site.register(Screens, ScreenAdmin)
