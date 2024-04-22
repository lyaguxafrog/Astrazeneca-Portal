# -*- coding: utf-8 -*-

from django.contrib import admin
from pages.models import LastAdds
from config.admin import custom_admin_site

admin.site = custom_admin_site

class LastAddAdmin(admin.ModelAdmin):
    list_display = (
        'content',
        'content_type'
    )


admin.site.register(LastAdds, LastAddAdmin)
