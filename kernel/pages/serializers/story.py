# -*- coding: utf-8 -*-

from rest_framework import serializers
from pages.models import Story

class StoryListSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Story
        fields = ['id', 'title', 'avatar']

    def get_avatar(self, obj):
        return self.get_relative_url(obj.avatar)

    def get_relative_url(self, field):
        return field.url if field else None

class StorySerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Story
        fields = '__all__'

    def get_avatar(self, obj):
        return self.get_relative_url(obj.avatar)

    def get_relative_url(self, field):
        return field.url if field else None
