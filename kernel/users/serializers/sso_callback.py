# -*- coding: utf-8 -*-

from rest_framework import serializers

class SsoCallbackSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()
    status = serializers.IntegerField()
