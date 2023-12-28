# -*- coding: utf-8 -*-

from rest_framework.generics import ListAPIView
from drf_haystack.viewsets import HaystackViewSet
from pages.models import Articles, Drug, VideoLectures
from pages.serializers import SearchResultsSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from drf_yasg import openapi



class SearchResultsView(ListAPIView, HaystackViewSet):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('query', openapi.IN_QUERY, description="Search query", type=openapi.TYPE_STRING)
        ]
    )

    @action(detail=False, methods=['get'])
    def list(self, request, *args, **kwargs):
        index_models = [Articles, Drug, VideoLectures]
        serializer_class = SearchResultsSerializer

        return super().list(request, *args, **kwargs)
