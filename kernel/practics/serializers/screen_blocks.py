# -*- coding: utf-8 -*-

from rest_framework import serializers

from practics.models import (ScreenPopupBlock,
                             ScreenButton, ScreenImageBlock,
                             ScreenTextBlock)



class LeftTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenTextBlock
        fields = '__all__'

class LeftImagesSerializer(serializers.ModelSerializer):
    image_desktop_810px = serializers.SerializerMethodField()
    image_desktop_1620px = serializers.SerializerMethodField()
    image_mobile_400px = serializers.SerializerMethodField()
    image_mobile_800px = serializers.SerializerMethodField()


    class Meta:
        model = ScreenImageBlock
        fields = '__all__'

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


class LeftPopUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenPopupBlock
        fields = '__all__'

class LeftButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenButton
