# -*- coding: utf-8 -*-

from rest_framework import serializers
from pages.models import Story
from django.db import models

class StoryListSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    video = serializers.SerializerMethodField()
    cover_image = serializers.SerializerMethodField()
    avatar_desktop_120px = serializers.SerializerMethodField()
    avatar_desktop_280px = serializers.SerializerMethodField()
    avatar_mobile_70px = serializers.SerializerMethodField()
    avatar_mobile_140px = serializers.SerializerMethodField()
    cover_450px = serializers.SerializerMethodField()
    cover_900px = serializers.SerializerMethodField()


    class Meta:
        model = Story
        fields = '__all__'
        ordering = ['id']

    def get_queryset(self):
        return Story.objects.all().order_by('id')

    def get_video(self, obj):
        return self.get_relative_url(obj.video)

    def get_cover_image(self, obj):
        return self.get_relative_url(obj.cover_image)

    def get_avatar(self, obj):
        return self.get_relative_url(obj.avatar)

    def get_avatar_desktop_120px(self, obj):
        return self.get_relative_url(obj.avatar_desktop_120px)

    def get_avatar_desktop_280px(self, obj):
        return self.get_relative_url(obj.avatar_desktop_280px)

    def get_avatar_mobile_70px(self, obj):
        return self.get_relative_url(obj.avatar_mobile_70px)

    def get_avatar_mobile_140px(self, obj):
        return self.get_relative_url(obj.avatar_mobile_140px)

    def get_cover_450px(self, obj):
        return self.get_relative_url(obj.cover_450px)

    def get_cover_900px(self, obj):
        return self.get_relative_url(obj.cover_900px)

    def get_relative_url(self, file_field_or_url):
        if file_field_or_url and hasattr(file_field_or_url, 'url'):
            return file_field_or_url.url
        elif isinstance(file_field_or_url, str) and file_field_or_url.startswith('http'):
            return file_field_or_url
        return None


class StorySerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    avatar_desktop_120px = serializers.SerializerMethodField()
    avatar_desktop_280px = serializers.SerializerMethodField()
    avatar_mobile_70px = serializers.SerializerMethodField()
    avatar_mobile_140px = serializers.SerializerMethodField()
    cover_450px = serializers.SerializerMethodField()
    cover_900px = serializers.SerializerMethodField()

    class Meta:
        model = Story
        fields = '__all__'
        ordering = ['id']


    def get_queryset(self):
        queryset = Story.objects.annotate(num_specialties=models.Count('specialties')).filter(num_specialties=0)

        return queryset

    def get_avatar(self, obj):
        return self.get_relative_url(obj.avatar)

    def get_avatar_desktop_120px(self, obj):
        return self.get_relative_url(obj.avatar_desktop_120px)

    def get_avatar_desktop_280px(self, obj):
        return self.get_relative_url(obj.avatar_desktop_280px)

    def get_avatar_mobile_70px(self, obj):
        return self.get_relative_url(obj.avatar_mobile_70px)

    def get_avatar_mobile_140px(self, obj):
        return self.get_relative_url(obj.avatar_mobile_140px)

    def get_cover_450px(self, obj):
        return self.get_relative_url(obj.cover_450px)

    def get_cover_900px(self, obj):
        return self.get_relative_url(obj.cover_900px)

    def get_relative_url(self, file_field_or_url):
        if file_field_or_url and hasattr(file_field_or_url, 'url'):
            return file_field_or_url.url
        elif isinstance(file_field_or_url, str) and file_field_or_url.startswith('http'):
            return file_field_or_url
        return None
