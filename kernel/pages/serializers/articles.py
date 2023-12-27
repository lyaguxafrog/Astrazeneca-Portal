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
    cover = serializers.SerializerMethodField()

    class Meta:
        model = Articles
        fields = '__all__'

    def get_cover(self, obj):
        return obj.cover.url if obj.cover else None

class ArticlesBySpecialitySerializer(serializers.ModelSerializer):
    cover = serializers.SerializerMethodField()


    class Meta:
        model = Articles
        fields = ['id', 'article_name', 'cover']


    def get_cover(self, obj):
        return obj.cover.url if obj.cover else None
