# -*- coding: utf-8 -*-

from rest_framework import serializers
from pages.models import Articles, Drug, VideoLectures, Events
from users.models import UserProfile

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

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'

class GetSavedContentViewSerializer(serializers.Serializer):
    message = serializers.CharField()
    saved_content = serializers.DictField()

class UserProfileSerializer(serializers.ModelSerializer):
    saved_content = serializers.JSONField()

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'saved_content', 'temporary_token', 'specialty']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        saved_content = instance.saved_content

        serialized_content = {}
        for content_type, content_ids in saved_content.items():
            if content_type == 'article':
                articles = Articles.objects.filter(id__in=content_ids)
                serialized_content['article'] = ArticleSerializer(articles, many=True).data
            elif content_type == 'video_lecture':
                video_lectures = VideoLectures.objects.filter(id__in=content_ids)
                serialized_content['video_lecture'] = VideoLecturesSerializer(video_lectures, many=True).data
            elif content_type == 'drug':
                drugs = Drug.objects.filter(id__in=content_ids)
                serialized_content['drug'] = DrugSerializer(drugs, many=True).data
            elif content_type == 'event':
                events = Events.objects.filter(id__in=content_ids)
                serialized_content['event'] = EventsSerializer(events, many=True).data
            # Добавьте обработку других типов контента здесь

        data['saved_content'] = serialized_content
        return data


class ContentSaveSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    content_type = serializers.CharField()
    content_id = serializers.IntegerField()

class GetSavedContentViewSerializer(serializers.Serializer):
    message = serializers.CharField()
    saved_content = serializers.DictField()
