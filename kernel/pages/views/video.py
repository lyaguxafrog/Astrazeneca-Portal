# -*- coding: utf-8 -*-

from rest_framework import generics
from pages.models import VideoLectures
from pages.serializers import VideoLecturesSerializer, VideoLecturesListSerializer

class VideoLecturesList(generics.ListAPIView):
    queryset = VideoLectures.objects.all()
    serializer_class = VideoLecturesListSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return VideoLectures.objects.filter(speciality__name=name)

class VideoLecturesDetail(generics.RetrieveAPIView):
    queryset = VideoLectures.objects.all()
    serializer_class = VideoLecturesSerializer
