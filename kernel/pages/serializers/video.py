# -*- coding: utf-8 -*-


from rest_framework import serializers
from pages.models import VideoLectures

class VideoLecturesSerializer(serializers.ModelSerializer):
    video_article_url = serializers.SerializerMethodField()
    video_url = serializers.SerializerMethodField()
    video_recomendations = serializers.SerializerMethodField()

    video_cover_desktop_1400px = serializers.SerializerMethodField()
    video_cover_desktop_2800px = serializers.SerializerMethodField()
    video_cover_mobile_420px = serializers.SerializerMethodField()
    video_cover_mobile_840px = serializers.SerializerMethodField()
    video_cover_mobile_390px = serializers.SerializerMethodField()
    video_cover_mobile_780px = serializers.SerializerMethodField()



    class Meta:
        model = VideoLectures
        fields = [
            'id',
            'video_article_url',
            'video_url',
            'video_article',
            'short_description',
            'conspect',
            'access_number',
            'content_type',
            'drug',
            'video_recomendations',
            'speciality',

            'video_cover_desktop_1400px',
            'video_cover_desktop_2800px',
            'video_cover_mobile_420px',
            'video_cover_mobile_840px',
            'video_cover_mobile_780px',
            'video_cover_mobile_390px'
        ]

    def get_video_cover_desktop_1400px(self, obj):
        return self.get_relative_url(obj.video_cover_desktop_1400px)

    def get_video_cover_desktop_2800px(self, obj):
        return self.get_relative_url(obj.video_cover_desktop_2800px)

    def get_recomendation_cover_desktop_430px(self, obj):
        return self.get_relative_url(obj.recomendation_cover_desktop_430px)

    def get_recomendation_cover_desktop_860px(self, obj):
        return self.get_relative_url(obj.recomendation_cover_desktop_860px)

    def get_video_cover_mobile_420px(self, obj):
        return self.get_relative_url(obj.video_cover_mobile_420px)

    def get_video_cover_mobile_840px(self, obj):
        return self.get_relative_url(obj.video_cover_mobile_840px)

    def get_recomendation_cover_mobile_270px(self, obj):
        return self.get_relative_url(obj.recomendation_cover_mobile_270px)

    def get_recomendation_cover_mobile_540px(self, obj):
        return self.get_relative_url(obj.recomendation_cover_mobile_540px)

    def get_video_cover_mobile_390px(self, obj):
        return self.get_relative_url(obj.video_cover_mobile_390px)

    def get_video_cover_mobile_780px(self, obj):
        return self.get_relative_url(obj.video_cover_mobile_780px)

    def get_video_article_url(self, obj):
        return self.get_relative_url(obj.video_article)

    def get_video_url(self, obj):
        return self.get_relative_url(obj.video)

    def get_video_recomendations(self, obj):
        return [
            {
                'id': recommendation.id,
                'title': recommendation.video_article,
                'recomendation_cover_desktop_500px': self.get_relative_url(recommendation.recomendation_cover_desktop_500px),
                'recomendation_cover_desktop_1000px': self.get_relative_url(recommendation.recomendation_cover_desktop_1000px),
                'recomendation_cover_mobile_280px': self.get_relative_url(recommendation.recomendation_cover_mobile_280px),
                'recomendation_cover_mobile_560px': self.get_relative_url(recommendation.recomendation_cover_mobile_560px),

            }
            for recommendation in obj.video_recomendations.all()
        ]

    def get_relative_url(self, file_field_or_url):
        if file_field_or_url and hasattr(file_field_or_url, 'url'):
            return file_field_or_url.url
        elif isinstance(file_field_or_url, str) and file_field_or_url.startswith('http'):
            return file_field_or_url
        return None


class VideoLecturesListSerializer(serializers.ModelSerializer):
    video_article_url = serializers.SerializerMethodField()
    video_cover_desktop_1400px = serializers.SerializerMethodField()
    video_cover_desktop_2800px = serializers.SerializerMethodField()
    video_cover_mobile_420px = serializers.SerializerMethodField()
    video_cover_mobile_840px = serializers.SerializerMethodField()


    class Meta:
        model = VideoLectures
        fields = ['id',
                  'video_article_url',
                  'content_type',
                  'speciality',
                  'priority',
                    'video_cover_desktop_1400px',
                    'video_cover_desktop_2800px',
                    'video_cover_mobile_420px',
                    'video_cover_mobile_840px',

            ]

    def get_video_cover_desktop_1400px(self, obj):
        return self.get_relative_url(obj.video_cover_desktop_1400px)

    def get_video_cover_desktop_2800px(self, obj):
        return self.get_relative_url(obj.video_cover_desktop_2800px)

    def get_video_cover_mobile_420px(self, obj):
        return self.get_relative_url(obj.video_cover_mobile_420px)

    def get_video_cover_mobile_840px(self, obj):
        return self.get_relative_url(obj.video_cover_mobile_840px)

    def get_video_article_url(self, obj):
        return self.get_relative_url(obj.video_article)

    def get_relative_url(self, file_field_or_url):
        if file_field_or_url:
            if hasattr(file_field_or_url, 'url'):
                return file_field_or_url.url
            elif isinstance(file_field_or_url, str):
                return file_field_or_url
        return None
