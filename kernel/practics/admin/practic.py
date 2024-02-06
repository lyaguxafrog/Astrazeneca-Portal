# -*- coding: utf-8 -*-

from django.contrib import admin
from config.admin import custom_admin_site

admin.site = custom_admin_site

from practics.models import (Practicum, Screens, Block, BlockEntity)
from nested_admin import (NestedModelAdmin,
                          NestedStackedInline,
                          NestedTabularInline)



# class ScreensInline(NestedStackedInline):
#     model = Screens
#     extra = 0




class PracticumAdmin(NestedModelAdmin):
    exclude = [
        'image_desktop_810px',
        'image_desktop_1620px',
        'image_mobile_400px',
        'image_mobile_800px']

    search_fields = ['title', 'desription', 'pacient_description']


admin.site.register(Practicum, PracticumAdmin)

