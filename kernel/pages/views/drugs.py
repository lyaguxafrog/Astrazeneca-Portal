# -*- coding: utf-8 -*-

from rest_framework import generics
from pages.models import Drug
from pages.serializers import DrugListSerializer, DrutSerializer

class DrugListAPIView(generics.ListAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugListSerializer

class DrugDetailAPIView(generics.RetrieveAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrutSerializer
