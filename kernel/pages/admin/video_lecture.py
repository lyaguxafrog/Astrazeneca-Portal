# -*- coding: utf-8 -*-

from tkinter import Widget
from django import forms
from django.contrib import admin
from pages.models import VideoLectures

class VideoLecturesAdminForm(forms.ModelForm):
    class Meta:
        model = VideoLectures
        exclude = []
        widgets = {
            'video_article': forms.Textarea(attrs={'rows': 2, 'cols': 52}),
        }

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
    fields = (
        'video_article',
        'short_description',
        'content_type',
        'video',
        'video_cover_desktop',
        'video_cover_mobile',
        'conspect',
        'video_recomendations',
        'drug',
        'speciality',
        'access_number'
    )
