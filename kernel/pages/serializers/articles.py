# -*- coding: utf-8 -*-

from rest_framework import serializers
from pages.models import Articles

class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'

class ArticlesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ['id', 'article_name']
