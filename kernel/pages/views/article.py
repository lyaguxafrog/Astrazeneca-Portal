# -*- coding: utf-8 -*-

from rest_framework import generics
from pages.models import Articles
from pages.serializers import ArticlesSerializer, ArticlesListSerializer

class ArticlesListAPIView(generics.ListAPIView):
    serializer_class = ArticlesListSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Articles.objects.filter(speciality__name=name)

class ArticlesDetailAPIView(generics.RetrieveAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
