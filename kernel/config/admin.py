# -*- coding: utf-8 -*-

from django.contrib import admin

class CustomAdminSite(admin.AdminSite):
    site_title = 'Astrazeneca Portal'
    site_header = 'Astrazeneca Portal'
    index_title = 'Главная страница'

custom_admin_site = CustomAdminSite(name='customadmin')
