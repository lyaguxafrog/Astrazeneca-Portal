# -*- coding: utf-8 -*-

from rest_framework import generics
from pages.models import Events
from pages.serializers import EventsSerializer, EventsListSerializer

class EventsListAPIView(generics.ListAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsListSerializer

class EventsDetailAPIView(generics.RetrieveAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
