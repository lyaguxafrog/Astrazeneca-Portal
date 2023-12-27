# -*- coding: utf-8 -*-


from django.contrib import admin
from pages.models import Drug, Icon, Articles, VideoLectures
from pages.services.forms import DrugForm, IconForm



from django.utils.html import format_html

class IconInline(admin.TabularInline):
    model = Icon
    extra = 1




class DrugAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_articles', 'display_videos')
    fields = ('name', 'brief_info', 'application_practice_articles',
              'application_practice_videos',
              'image', 'instruction_text', 'approvals_and_decodings', 'icons')
    inlines = [IconInline]

    def display_articles(self, obj):
        return ", ".join([article.article_name for article in obj.application_practice_articles.all()])

    display_articles.short_description = 'Application Practice Articles'
    def display_videos(self, obj):
        return ", ".join([video.video_article for video in obj.application_practice_videos.all()])

    display_videos.short_description = 'Application Practice Videos'

admin.site.register(Drug, DrugAdmin)
