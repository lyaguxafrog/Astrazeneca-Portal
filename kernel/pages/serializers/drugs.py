# -*- coding: utf-8 -*-


from rest_framework import serializers
from pages.models import Drug, Icon, DrugFAQ
from urllib.parse import urlparse



class DrugListSerializer(serializers.ModelSerializer):
    image_desktop_1400px = serializers.SerializerMethodField()
    image_desktop_700px = serializers.SerializerMethodField()
    image_mobile_270px = serializers.SerializerMethodField()
    image_mobile_540px = serializers.SerializerMethodField()

    class Meta:
        model = Drug
        fields = [
            'id',
            'name',
            'brief_info',
            'image_desktop_1400px',
            'image_desktop_700px',
            'image_mobile_270px',
            'image_mobile_540px',
                  ]

    def get_image_desktop_1400px(self, obj):
        return self.get_relative_url(obj.image_desktop_1400px)

    def get_image_desktop_700px(self, obj):
        return self.get_relative_url(obj.image_desktop_700px)

    def get_image_mobile_270px(self, obj):
        return self.get_relative_url(obj.image_mobile_270px)

    def get_image_mobile_540px(self, obj):
        return self.get_relative_url(obj.image_mobile_540px)

    def get_relative_url(self, file_field_or_url):
        if file_field_or_url and hasattr(file_field_or_url, 'url'):
            return file_field_or_url.url
        elif isinstance(file_field_or_url, str) and file_field_or_url.startswith('http'):
            return file_field_or_url
        return None

class IconSerializer(serializers.ModelSerializer):
    image_file = serializers.SerializerMethodField()

    class Meta:
        model = Icon
        fields = ['id', 'image_file']

    def get_image_file(self, obj):
        return obj.image_file.url if obj.image_file else None

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugFAQ
        fields = ['title',
                  'text',
                  'order']


class DrugSerializer(serializers.ModelSerializer):
    icons = IconSerializer(many=True, read_only=True)
    faq = FAQSerializer(many=True, read_only=True)
    application_practices = serializers.SerializerMethodField()
    image_desktop_1400px = serializers.SerializerMethodField()
    image_desktop_700px = serializers.SerializerMethodField()
    image_mobile_270px = serializers.SerializerMethodField()
    image_mobile_540px = serializers.SerializerMethodField()


    class Meta:
        model = Drug
        fields = [
            "id",
            "icons",
            "faq",
            "application_practices",
            "image_desktop_1400px",
            "image_desktop_700px",
            "image_mobile_270px",
            "image_mobile_540px",
            "name",
            "brief_info",
            "approvals_and_decodings",
            "url_field",
            "file_field",
            "speciality"
        ]

    def get_image_desktop_1400px(self, obj):
        return self.get_relative_url(obj.image_desktop_1400px)

    def get_image_desktop_700px(self, obj):
        return self.get_relative_url(obj.image_desktop_700px)

    def get_image_mobile_270px(self, obj):
        return self.get_relative_url(obj.image_mobile_270px)

    def get_image_mobile_540px(self, obj):
        return self.get_relative_url(obj.image_mobile_540px)

    def get_relative_url(self, file_field_or_url):
        if file_field_or_url and hasattr(file_field_or_url, 'url'):
            return file_field_or_url.url
        elif isinstance(file_field_or_url, str) and file_field_or_url.startswith('http'):
            return file_field_or_url
        return None


    def get_application_practices(self, obj):
        articles = obj.application_practice_articles.all()
        videos = obj.application_practice_videos.all()

        # Combine articles and videos into a single list
        combined_practices = []
        for article in articles:
            combined_practices.append({
                'id': article.id,
                'type': 'article',
                'cover_desktop_1400px': article.cover_desktop_1400px.url if article.cover_desktop_1400px else None,
                'cover_desktop_2800px': article.cover_desktop_2800px.url if article.cover_desktop_2800px else None,
                'cover_mobile_420px': article.cover_mobile_420px.url if article.cover_mobile_420px else None,
                'cover_mobile_840px': article.cover_mobile_840px.url if article.cover_mobile_840px else None,
                'name': article.article_name,
            })

        for video in videos:
            combined_practices.append({
                'id': video.id,
                'type': 'video',
                'name': video.video_article,
                'video_cover_desktop_1400px': video.video_cover_desktop_1400px.url if video.video_cover_desktop_1400px else None,
                'video_cover_desktop_2800px': video.video_cover_desktop_2800px.url if video.video_cover_desktop_2800px else None,
                'recomendation_cover_desktop_430px': video.recomendation_cover_desktop_430px.url if video.recomendation_cover_desktop_430px else None,
                'recomendation_cover_desktop_860px': video.recomendation_cover_desktop_860px.url if video.recomendation_cover_desktop_860px else None,
                'video_cover_mobile_420px': video.video_cover_mobile_420px.url if video.video_cover_mobile_420px else None,
                'video_cover_mobile_840px': video.video_cover_mobile_840px.url if video.video_cover_mobile_840px else None,
                'recomendation_cover_mobile_270px': video.recomendation_cover_mobile_270px.url if video.recomendation_cover_mobile_270px else None,
                'recomendation_cover_mobile_540px': video.recomendation_cover_mobile_540px.url if video.recomendation_cover_mobile_540px else None,
            })

        return combined_practices
