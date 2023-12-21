# -*- coding: utf-8 -*-

from rest_framework import generics
from pages.models import Articles
from pages.serializers import ArticlesSerializer

class ArticlesListAPIView(generics.ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer

class ArticlesDetailAPIView(generics.RetrieveAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
