# -*- coding: utf-8 -*-

from rest_framework import generics, response

from practics.models import PrTest
from practics.serializers import PrTestListSerializer


class PrTestListAPIView(generics.ListAPIView):
    """ API View для обображения списка тестов """

    serializer_class = PrTestListSerializer

    def get_queryset(self):
        return PrTest.objects.all().order_by('priority')
