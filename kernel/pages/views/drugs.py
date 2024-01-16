# -*- coding: utf-8 -*-

from rest_framework import generics, response
from pages.models import Drug
from pages.serializers import (DrugListSerializer, DrugSerializer,
                               IconSerializer, FAQSerializer)

class DrugListAPIView(generics.ListAPIView):
    serializer_class = DrugListSerializer

    def get_queryset(self):
        return Drug.objects.all().order_by('priority')

class DrugDetailAPIView(generics.RetrieveAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data

        faq = instance.faq.all()
        faq_serializer = FAQSerializer(faq, many=True)
        data['faq'] = faq_serializer.data

        icons = instance.icons.all()
        icons_serializer = IconSerializer(icons, many=True)
        data['icons'] = icons_serializer.data

        return response.Response(data)
