# -*- coding: utf-8 -*-

from rest_framework import generics, response
from pages.models import Articles
from pages.serializers import (ArticlesSerializer, ContentBlockSerializer,
                               ArticlesBySpecialitySerializer)

class ArticleDetailAPIView(generics.RetrieveAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    lookup_url_kwarg = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data

        # Добавляем ContentBlocks в данные ответа
        content_blocks = instance.content_blocks.all()
        content_blocks_serializer = ContentBlockSerializer(content_blocks, many=True)
        data['content_blocks'] = content_blocks_serializer.data

        return response.Response(data)



class ArticlesBySpecialtyAPIView(generics.ListAPIView):
    serializer_class = ArticlesBySpecialitySerializer

    def get_queryset(self):
        specialty_id = self.kwargs['specialty_id']
        queryset = Articles.objects.filter(speciality__id=specialty_id)
        return queryset
