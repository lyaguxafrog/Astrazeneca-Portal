# -*- coding: utf-8 -*-

from django.contrib import admin
from pages.models import LastAdds


@admin.register(LastAdds)
class LastAddAdmin(admin.ModelAdmin):
    list_display = (
        'content',
        'content_type'
    )
