# -*- coding: utf-8 -*-

from django import forms
from django.contrib import admin
from pages.models import VideoLectures

class VideoLecturesAdminForm(forms.ModelForm):
    class Meta:
        model = VideoLectures
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            # Exclude the currently edited video from video_recomendations
            self.fields['video_recomendations'].queryset = VideoLectures.objects.exclude(id=instance.id)

@admin.register(VideoLectures)
class VideoLecturesAdmin(admin.ModelAdmin):
    list_display = ("video_article", "content_type")
    form = VideoLecturesAdminForm
