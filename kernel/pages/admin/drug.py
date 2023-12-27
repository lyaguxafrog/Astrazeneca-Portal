# -*- coding: utf-8 -*-


from django.contrib import admin
from pages.models import Drug, Icon
from pages.services.forms import DrugForm, IconForm


class IconInline(admin.TabularInline):
    model = Icon
    extra = 1

class DrugAdmin(admin.ModelAdmin):
    inlines = [IconInline]

admin.site.register(Drug, DrugAdmin)
