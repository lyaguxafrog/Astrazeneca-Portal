# -*- config: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from users.models import UserProfile

from config.admin import custom_admin_site

admin.site = custom_admin_site

# Создаем Inline-класс для редактирования UserProfile вместе с моделью User
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profile'

# Расширяем стандартную модель User для отображения UserProfile
class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

# Регистрируем модели в административной панели
# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)
