# -*- coding: utf-8 -*-

from rest_framework import generics
from pages.models import Story
from pages.serializers import StorySerializer, StoryListSerializer
from django.db.models import Q

class StoryListAPIView(generics.ListAPIView):
    serializer_class = StoryListSerializer

    def get_queryset(self):
        specialty_id = self.kwargs.get('id')  # Извлекаем id специальности из URL-параметров

        if specialty_id:
            # Если передан id специальности, фильтруем истории по специальности
            return Story.objects.filter(specialties__id=specialty_id, is_active=True)
        else:
            # Если id специальности не передан, возвращаем все истории
            return Story.objects.filter(is_active=True)

class SpecialityStoryListAPIView(generics.ListAPIView):
    serializer_class = StoryListSerializer

    def get_queryset(self):
        specialty_id = self.kwargs.get('id')

        if specialty_id:
            # Если передан id специальности, фильтруем истории по специальности и тем, которые не привязаны
            return Story.objects.filter(Q(specialties__id=specialty_id) | Q(specialties__isnull=True), is_active=True)
        else:
            # Если id специальности не передан, возвращаем все истории
            return Story.objects.filter(is_active=True)


class StoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    lookup_field = 'id'
