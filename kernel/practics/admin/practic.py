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
