# -*- coding: utf-8 -*-

from rest_framework import serializers
from pages.models import Story

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'
