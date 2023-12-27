# -*- coding: utf-8 -*-


from rest_framework import serializers
from pages.models import (Articles, ContentBlock, Drug, Icon, Events,
                          VideoLectures)

class SearchContentBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentBlock
        fields = '__all__'

class SearchArticleSerializer(serializers.ModelSerializer):
    content_blocks = SearchContentBlockSerializer(many=True, read_only=True)

    class Meta:
        model = Articles
        fields = [
            'id',
            'article_name',
            'cover',
            'final_content',
            'access_number',
            'speciality',
            'drug',
            'article_type',
            'content_blocks',
        ]


class IconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Icon
        fields = ['id', 'image_file']

class SearchDrugSerializer(serializers.ModelSerializer):
    icons = IconSerializer(many=True, read_only=True)

    class Meta:
        model = Drug
        fields = [
            'id',
            'name',
            'brief_info',
            'image',
            'instruction_text',
            'application_practice_articles',
            'application_practice_videos',
            'approvals_and_decodings',
            'icons',
        ]

class SearchEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = [
            'id',
            'name',
            'date',
            'cover',
            'text',
            'url',
        ]


class SearchVideoLecturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLectures
        fields = '__all__'
