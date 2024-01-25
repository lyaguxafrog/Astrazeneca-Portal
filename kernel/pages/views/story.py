# -*- coding: utf-8 -*-

from rest_framework import generics
from pages.models import Story
from pages.serializers import StorySerializer, StoryListSerializer
from django.db.models import Q

class StoryListAPIView(generics.ListAPIView):
    serializer_class = StoryListSerializer

    def get_queryset(self):
        specialty_id = self.kwargs.get('id')

        if specialty_id:
            queryset = Story.objects.filter(specialties__id=specialty_id, is_active=True).exclude(specialties__isnull=False)
        else:
            queryset = Story.objects.filter(is_active=True).exclude(specialties__isnull=False)

        # Add sorting by id
        queryset = queryset.order_by('id')

        return queryset

class SpecialityStoryListAPIView(generics.ListAPIView):
    serializer_class = StoryListSerializer

    def get_queryset(self):
        specialty_id = self.kwargs.get('id')

        if specialty_id:
            queryset = Story.objects.filter(
                Q(specialties__id=specialty_id) | Q(specialties__isnull=True),
                is_active=True
            )
        else:
            queryset = Story.objects.filter(is_active=True)

        queryset = queryset.order_by('id')

        return queryset

class StoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    lookup_field = 'id'
