# -*- coding: utf-8 -*-


from rest_framework import serializers
from pages.models import Events

class EventsSerializer(serializers.ModelSerializer):

    image_1400px = serializers.SerializerMethodField()
    image_2800px = serializers.SerializerMethodField()
    image_390px = serializers.SerializerMethodField()
    image_780px = serializers.SerializerMethodField()


    def get_image_1400px(self, obj):
        return self.get_relative_url(obj.image_1400px)

    def get_image_2800px(self, obj):
        return self.get_relative_url(obj.image_2800px)

    def get_image_390px(self, obj):
        return self.get_relative_url(obj.image_390px)

    def get_image_780px(self, obj):
        return self.get_relative_url(obj.image_780px)

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
        # Update the 'cover' field to contain the relative path
        representation['cover'] = instance.cover.url if instance.cover else None
        return representation
