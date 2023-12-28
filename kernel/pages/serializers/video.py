# -*- coding: utf-8 -*-


from rest_framework import serializers
from pages.models import VideoLectures

class VideoLecturesSerializer(serializers.ModelSerializer):
    video_cover_url = serializers.SerializerMethodField()
    video_article_url = serializers.SerializerMethodField()
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = VideoLectures
        fields = ['id', 'video_cover_url', 'video_article_url', 'video_url', 'video_article', 'short_description', 'conspect', 'video', 'video_cover', 'access_number', 'content_type', 'drug', 'video_recomendations', 'speciality']

    def get_video_cover_url(self, obj):
        return self.get_relative_url(obj.video_cover)

    def get_video_article_url(self, obj):
        return self.get_relative_url(obj.video_article)

    def get_video_url(self, obj):
        return self.get_relative_url(obj.video)

    def get_relative_url(self, file_field_or_url):
        if file_field_or_url and hasattr(file_field_or_url, 'url'):
            # If it's a FileField or ImageField, return the relative path
            return file_field_or_url.url
        elif isinstance(file_field_or_url, str) and file_field_or_url.startswith('http'):
            # If it's a string (URL) starting with 'http', consider it an external URL
            return file_field_or_url
        return None



class VideoLecturesListSerializer(serializers.ModelSerializer):
    video_cover_url = serializers.SerializerMethodField()
    video_article_url = serializers.SerializerMethodField()

    class Meta:
        model = VideoLectures
        fields = ['id', 'video_cover_url', 'video_article_url', 'content_type', 'speciality']

    def get_video_cover_url(self, obj):
        return self.get_relative_url(obj.video_cover)

    def get_video_article_url(self, obj):
        return self.get_relative_url(obj.video_article)

    def get_relative_url(self, file_field_or_url):
        if file_field_or_url:
            if hasattr(file_field_or_url, 'url'):
                # If it's a FileField or ImageField, return the relative path
                return file_field_or_url.url
            elif isinstance(file_field_or_url, str):
                # If it's a string (URL), return it as is
                return file_field_or_url
        return None
