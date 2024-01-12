# -*- coding: utf-8 -*-

from rest_framework import serializers
from users.models import UserProfile


class SsoCallbackSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()
    status = serializers.IntegerField()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['sso_user_id', 'access_token',
                  'refresh_token', 'token_expiry']
