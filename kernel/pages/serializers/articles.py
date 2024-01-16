# -*- coding: utf-8 -*-

from rest_framework import serializers
from pages.models import Articles, ContentBlock

class ContentBlockSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ContentBlock
        fields = '__all__'

    def get_image(self, obj):
        return obj.image.url if obj.image else None

class ArticlesSerializer(serializers.ModelSerializer):
    content_blocks = ContentBlockSerializer(many=True, read_only=True)
    cover_desktop_1400px = serializers.SerializerMethodField()
    cover_desktop_2800px = serializers.SerializerMethodField()
    cover_mobile_840px = serializers.SerializerMethodField()
    cover_mobile_420px = serializers.SerializerMethodField()

    main_cover_desktop_1600px = serializers.SerializerMethodField()
    main_cover_desktop_3200px = serializers.SerializerMethodField()
    main_cover_mobile_360px = serializers.SerializerMethodField()
    main_cover_mobile_720px = serializers.SerializerMethodField()

    class Meta:
        model = Articles
        fields = [
            'id',
            'article_name',
            'center_title',
            'information',
            'first_abzac',
            'content_blocks',
            'speciality',
            'drug',
            'cover_desktop_1400px',
            'cover_desktop_2800px',
            'cover_mobile_840px',
            'cover_mobile_420px',
            'main_cover_desktop_1600px',
            'main_cover_desktop_3200px',
            'main_cover_mobile_360px',
            'main_cover_mobile_720px',
            'final_content',
            'access_number'
            ]

        ordering = ['priority']


    def get_cover_desktop_1400px(self, obj):
        return self.get_relative_url(obj.main_cover_desktop_1600px)

    def get_cover_desktop_2800px(self, obj):
        return self.get_relative_url(obj.cover_desktop_2800px)

    def get_cover_mobile_840px(self, obj):
        return self.get_relative_url(obj.cover_mobile_840px)

    def get_cover_mobile_420px(self, obj):
        return self.get_relative_url(obj.cover_mobile_420px)

    def get_main_cover_desktop_1600px(self, obj):
        return self.get_relative_url(obj.main_cover_desktop_1600px)

    def get_main_cover_desktop_3200px(self, obj):
        return self.get_relative_url(obj.main_cover_desktop_3200px)

    def get_main_cover_mobile_360px(self, obj):
        return self.get_relative_url(obj.main_cover_mobile_360px)

    def get_main_cover_mobile_720px(self, obj):
        return self.get_relative_url(obj.main_cover_mobile_720px)

    def get_relative_url(self, file_field_or_url):
        if file_field_or_url and hasattr(file_field_or_url, 'url'):
            return file_field_or_url.url
        elif isinstance(file_field_or_url, str) and file_field_or_url.startswith('http'):
            return file_field_or_url
        return None


class ArticlesBySpecialitySerializer(serializers.ModelSerializer):
    cover_desktop_1400px = serializers.SerializerMethodField()
    cover_desktop_2800px = serializers.SerializerMethodField()
    cover_mobile_840px = serializers.SerializerMethodField()
    cover_mobile_420px = serializers.SerializerMethodField()


    class Meta:
        model = Articles
        fields = ['id', 'article_name', 'cover_desktop_1400px',
                  'cover_desktop_2800px', 'cover_mobile_840px', 'cover_mobile_420px',
                  'information', 'first_abzac', 'priority', 'center_title']



    def get_cover_desktop_1400px(self, obj):
        return self.get_relative_url(obj.cover_desktop_1400px)

    def get_cover_desktop_2800px(self, obj):
        return self.get_relative_url(obj.cover_desktop_2800px)

    def get_cover_mobile_840px(self, obj):
        return self.get_relative_url(obj.cover_mobile_840px)

    def get_cover_mobile_420px(self, obj):
        return self.get_relative_url(obj.cover_mobile_420px)

    def get_relative_url(self, file_field_or_url):
        if file_field_or_url and hasattr(file_field_or_url, 'url'):
            return file_field_or_url.url
        elif isinstance(file_field_or_url, str) and file_field_or_url.startswith('http'):
            return file_field_or_url
        return None
