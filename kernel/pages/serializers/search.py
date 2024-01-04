# -*- coding: utf-8 -*-

from rest_framework import serializers

class SearchSerializer(serializers.Serializer):
    title = serializers.SerializerMethodField()
    model = serializers.CharField()
    id = serializers.IntegerField()
    url = serializers.URLField(required=False)  # Make the URL field optional

    def get_title(self, instance):
        model_name = instance['model']
        if model_name == 'article':
            return instance.get('article_name', '')
        elif model_name == 'content_block':
            return instance.get('text', '')
        elif model_name == 'drug':
            return instance.get('name', '')
        elif model_name == 'drug_faq':
            return instance.get('title', '')
        elif model_name == 'event':
            return instance.get('name', '')
        elif model_name == 'video_lecture':
            return instance.get('video_article', '')
        return ''

    class Meta:
        fields = ['title', 'model', 'id', 'url']
