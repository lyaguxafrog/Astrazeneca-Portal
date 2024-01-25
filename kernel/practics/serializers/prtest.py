# -*- coding: utf-8 -*-

from rest_framework import serializers
from urllib.parse import urlparse

from practics.models import PrTest, AnswerButtons

class PrTestListSerializer(serializers.ModelSerializer):
    """ Сериализатор для отображения списка тестов """

    image_desktop_810px = serializers.SerializerMethodField()
    image_desktop_1620px = serializers.SerializerMethodField()
    image_mobile_400px = serializers.SerializerMethodField()
    image_mobile_800px = serializers.SerializerMethodField()

    class Meta:
        model = PrTest
        fields = ['id',
                  'title',
                  'question',
                  'priority',
                  'image',
                  'image_desktop_810px',
                  'image_desktop_1620px',
                  'image_mobile_400px',
                  'image_mobile_800px']


    def get_image_desktop_810px(self, obj):
        return self.get_relative_url(obj.image_desktop_810px)

    def get_image_desktop_1620px(self, obj):
        return self.get_relative_url(obj.image_desktop_1620px)

    def get_image_mobile_400px(self, obj):
        return self.get_relative_url(obj.image_mobile_400px)

    def get_image_mobile_800px(self, obj):
        return self.get_relative_url(obj.image_mobile_800px)

    def get_relative_url(self, file_field_or_url):
        if file_field_or_url and hasattr(file_field_or_url, 'url'):
            return file_field_or_url.url
        elif isinstance(file_field_or_url,
        str) and file_field_or_url.startswith('http'):
            return file_field_or_url
        return None


class AnswerButtonsSerializer(serializers.ModelSerializer):
    """ Сериализатор для кнопок с ответами """

    class Meta:
        model = AnswerButtons
        fields = [
            'title',
            'text',
        ]

class PrTestDetailSerializer(serializers.ModelSerializer):
    """ Сериализатор для детального просмотра теста """

    buttons = AnswerButtonsSerializer(many=True, read_only=True)
    image_desktop_810px = serializers.SerializerMethodField()
    image_desktop_1620px = serializers.SerializerMethodField()
    image_mobile_400px = serializers.SerializerMethodField()
    image_mobile_800px = serializers.SerializerMethodField()

    class Meta:
        model = PrTest
        fields = ['id',
                  'title',
                  'question',
                  'priority',
                  'buttons',
                  'image',
                  'image_desktop_810px',
                  'image_desktop_1620px',
                  'image_mobile_400px',
                  'image_mobile_800px']


    def get_image_desktop_810px(self, obj):
        return self.get_relative_url(obj.image_desktop_810px)

    def get_image_desktop_1620px(self, obj):
        return self.get_relative_url(obj.image_desktop_1620px)

    def get_image_mobile_400px(self, obj):
        return self.get_relative_url(obj.image_mobile_400px)

    def get_image_mobile_800px(self, obj):
        return self.get_relative_url(obj.image_mobile_800px)

    def get_relative_url(self, file_field_or_url):
        if file_field_or_url and hasattr(file_field_or_url, 'url'):
            return file_field_or_url.url
        elif isinstance(file_field_or_url,
        str) and file_field_or_url.startswith('http'):
            return file_field_or_url
        return None
