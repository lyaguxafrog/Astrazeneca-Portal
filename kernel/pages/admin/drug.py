# -*- coding: utf-8 -*-


from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from ckeditor.widgets import CKEditorWidget
from django.forms import Textarea
from pages.models import Drug, Icon, DrugFAQ
from django.db import models

class IconInline(admin.TabularInline):
    model = Icon
    extra = 1
    verbose_name = 'Иконка'
    verbose_name_plural = 'Иконки'

class Drug_FAQInline(admin.TabularInline):
    model = DrugFAQ
    extra = 1
    formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows': 2, 'cols': 80})},
        models.TextField: {'widget': CKEditorWidget()},
    }
    verbose_name = "Инструкцию"
    verbose_name_plural = "пункт"

class DrugAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_articles', 'display_videos')
    fields = ('name', 'brief_info', 'application_practice_articles',
              'application_practice_videos', 'image', 'approvals_and_decodings', 'url_field', 'icons', 'faq')
    inlines = [Drug_FAQInline, IconInline]

    def display_articles(self, obj):
        return ", ".join([article.article_name for article in obj.application_practice_articles.all()])

    display_articles.short_description = 'Application Practice Articles'

    def display_videos(self, obj):
        return ", ".join([video.video_article for video in obj.application_practice_videos.all()])

    display_videos.short_description = 'Application Practice Videos'

admin.site.register(Drug, DrugAdmin)
