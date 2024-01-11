# -*- coding: utf-8 -*-

from rest_framework import serializers
from pages.models import Articles, Drug, VideoLectures, Events, Story
from users.models import UserProfile
from collections import OrderedDict


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'

class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'

class VideoLecturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLectures
        fields = '__all__'

class GetSavedContentViewSerializer(serializers.Serializer):
    message = serializers.CharField()
    saved_content = serializers.DictField()

class UserProfileSerializer(serializers.ModelSerializer):
    saved_content = serializers.JSONField()

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'saved_content', 'temporary_token', 'specialty']

class ContentSaveSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    content_type = serializers.CharField()
    content_id = serializers.IntegerField()

class GetSavedContentViewSerializer(serializers.Serializer):
    message = serializers.CharField()
    saved_content = serializers.DictField()


class ContentRemoveSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    content_type = serializers.CharField()
    content_id = serializers.IntegerField()
