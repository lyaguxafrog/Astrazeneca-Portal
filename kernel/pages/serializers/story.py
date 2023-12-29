# -*- coding: utf-8 -*-

from rest_framework import serializers
from pages.models import Story
from django.db import models

class StoryListSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    def get_queryset(self):
        # Получите идентификатор специальности из URL
        specialty_id = self.kwargs['specialty_id']

        # Отфильтруйте истории на основе указанной специальности
        queryset = Story.objects.filter(specialties__id=specialty_id).distinct()

        return queryset

    class Meta:
        model = Story
        fields = ['id', 'title', 'avatar']

    def get_avatar(self, obj):
        return self.get_relative_url(obj.avatar)

    def get_relative_url(self, field):
        return field.url if field else None

class StorySerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Story
        fields = '__all__'


    def get_queryset(self):
        queryset = Story.objects.annotate(num_specialties=models.Count('specialties')).filter(num_specialties=0)

        return queryset

    def get_avatar(self, obj):
        return self.get_relative_url(obj.avatar)

    def get_relative_url(self, field):
        return field.url if field else None
