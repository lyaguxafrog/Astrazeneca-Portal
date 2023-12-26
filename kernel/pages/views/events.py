# -*- coding: utf-8 -*-

from rest_framework import generics
from pages.models import Events
from pages.serializers import EventsSerializer

class EventsAPIView(generics.ListAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
