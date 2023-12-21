# -*- coding: utf-8 -*-

from rest_framework import generics
from pages.models import Story
from pages.serializers import StorySerializer

class StoryListAPIView(generics.ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
