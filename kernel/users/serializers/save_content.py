# -*- coding: utf-8 -*-

from rest_framework import serializers

class ContentSaveSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    content_type = serializers.CharField()
    content_id = serializers.IntegerField()
