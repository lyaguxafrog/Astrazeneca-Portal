# -*- coding: utf-8 -*-

from rest_framework import generics, status
from rest_framework.response import Response
from django.http import Http404


from pages.models import Story
from pages.serializers import StorySerializer, StoryListSerializer

class StoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    lookup_field = 'id'

class StoryListAPIView(generics.ListAPIView):
    serializer_class = StoryListSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Story.objects.filter(specialties__name=name)
