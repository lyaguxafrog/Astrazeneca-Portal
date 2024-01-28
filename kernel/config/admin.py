# -*- coding: utf-8 -*-

from django.contrib import admin

class CustomAdminSite(admin.AdminSite):
    site_title = 'Ваш новый заголовок'
    site_header = 'Ваш новый заголовок'
    index_title = 'Главная страница'

custom_admin_site = CustomAdminSite(name='customadmin')
