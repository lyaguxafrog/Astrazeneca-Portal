# -*- coding: utf-8 -*-

from rest_framework import serializers
from pages.models import Articles, Drug, VideoLectures, Story
from users.models import UserProfile


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = [
            'id',
            'article_name',
            'favorite_desktop_300px',
            'favorite_desktop_600px',
            'favorite_mobile_250px',
            'favorite_mobile_500px'
        ]

# class DrugSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Drug
#         fields = [
#             'id',
#             'name',
#             'favorite_desktop_300px',
#             'favorite_desktop_600px',
#             'favorite_mobile_250px',
#             'favorite_mobile_500px'
#         ]

class StorySerializer(serializers.ModelSerializer):
    favorite_desktop_120px = serializers.ImageField(source='avatar_desktop_120px')
    favorite_desktop_280px = serializers.ImageField(source='avatar_desktop_280px')
    favorite_mobile_70x = serializers.ImageField(source='avatar_mobile_70px')
    favorite_mobile_140px = serializers.ImageField(source='avatar_mobile_140px')
    class Meta:
        model = Story
        fields = [
            'id',
            'title',
            'favorite_desktop_120px',
            'favorite_desktop_280px',
            'favorite_mobile_70x',
            'favorite_mobile_140px'
        ]

class VideoLecturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLectures
        fields = [
            'id',
            'video_article',
            'content_type',
            'favorite_desktop_300px',
            'favorite_desktop_600px',
            'favorite_mobile_250px',
            'favorite_mobile_500px'
        ]

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
