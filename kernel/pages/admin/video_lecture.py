# -*- coding: utf-8 -*-

from django.contrib import admin
from pages.models import VideoLectures


@admin.register(VideoLectures)
class VideoLecturesAdmin(admin.ModelAdmin):
    list_display = (
        "video_article",
        "content_type"
    )
