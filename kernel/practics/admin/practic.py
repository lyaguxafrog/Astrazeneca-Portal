# -*- coding: utf-8 -*-

from django.contrib import admin
from config.admin import custom_admin_site

admin.site = custom_admin_site

from practics.models import (Practicum, Screens, RBlock1, RBlock2)
from nested_admin import (NestedModelAdmin,
                          NestedStackedInline,
                          NestedTabularInline)
from polymorphic.admin import PolymorphicInlineSupportMixin, StackedPolymorphicInline



class ScreensInline(StackedPolymorphicInline):
    model = Screens
    extra = 0

    class RBloc1kInline(StackedPolymorphicInline.Child):
        model = RBlock1

    class RBlock2Inline(StackedPolymorphicInline.Child):
        model = RBlock2

    child_inlines = (
        RBloc1kInline,
        RBlock2Inline
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
