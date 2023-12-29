# -*- coding: utf-8 -*-

from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from pages.models import MainPageApproveNumber


class MainPageAdmin(admin.ModelAdmin):
    list_display = (
        'number',
    )



admin.site.register(MainPageApproveNumber, MainPageAdmin)
