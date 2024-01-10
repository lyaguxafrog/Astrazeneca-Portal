# -*- coding: utf-8 -*-


from rest_framework import serializers
from pages.models import Events

class EventsSerializer(serializers.ModelSerializer):

    image_desktop_1400px = serializers.SerializerMethodField()
    image_desktop_570px = serializers.SerializerMethodField()
    image_mobile_540px = serializers.SerializerMethodField()
    image_mobile_270px = serializers.SerializerMethodField()


    def get_image_desktop_1400px(self, obj):
        return self.get_relative_url(obj.image_desktop_1400px)

    def get_image_desktop_570px(self, obj):
        return self.get_relative_url(obj.image_desktop_570px)

    def get_image_mobile_540px(self, obj):
        return self.get_relative_url(obj.image_mobile_540px)

    def get_image_mobile_270px(self, obj):
        return self.get_relative_url(obj.image_mobile_270px)

    def get_image(self, obj):
        return obj.image.url if obj.image else None

    def get_relative_url(self, file_field_or_url):
        if file_field_or_url and hasattr(file_field_or_url, 'url'):
            return file_field_or_url.url
        elif isinstance(file_field_or_url, str) and file_field_or_url.startswith('http'):
            return file_field_or_url
        return None

    class Meta:
        model = Events
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['cover'] = instance.cover.url if instance.cover else None
        return representation
