# -*- coding: utf-8 -*-

from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from pages.models import MainPageApproveNumber
from config.admin import custom_admin_site

admin.site = custom_admin_site

class MainPageAdmin(admin.ModelAdmin):
    list_display = (
        'number',
    )



admin.site.register(MainPageApproveNumber, MainPageAdmin)
