# -*- coding: utf-8 -*-


from rest_framework import serializers
from pages.models import Specialty, Story


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'

class StoryCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'author', 'avatar',
                  'title', 'content', 'video',
                  'cover_image', 'link_to_page',
                  'specialties', 'is_active']

        read_only_fields = ['author']


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'author', 'avatar', 'title',
                  'content', 'video', 'cover_image',
                  'link_to_page', 'specialties', 'is_active']
