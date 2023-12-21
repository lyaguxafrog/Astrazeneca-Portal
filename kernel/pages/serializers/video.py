# -*- coding: utf-8 -*-


from rest_framework import serializers
from pages.models import VideoLectures

class VideoLecturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLectures
        fields = '__all__'


class VideoLecturesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLectures
        fields = ['id', 'video_article', 'content_type', 'speciality']
