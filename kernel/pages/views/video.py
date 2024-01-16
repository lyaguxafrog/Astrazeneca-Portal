# -*- coding: utf-8 -*-

from rest_framework import generics
from pages.models import VideoLectures
from pages.serializers import VideoLecturesSerializer, VideoLecturesListSerializer

class VideoLecturesListBySpecialty(generics.ListAPIView):
    serializer_class = VideoLecturesListSerializer

    def get_queryset(self):
        speciality_id = self.kwargs['id']
        queryset = VideoLectures.objects.filter(speciality__id=speciality_id)

        queryset = queryset.order_by('priority')

        return queryset

class VideoLecturesList(generics.ListAPIView):
    serializer_class = VideoLecturesListSerializer

    def get_queryset(self):
        return VideoLectures.objects.all().order_by('priority')

class VideoLecturesDetail(generics.RetrieveAPIView):
    queryset = VideoLectures.objects.all()
    serializer_class = VideoLecturesSerializer
