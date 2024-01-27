# -*- coding: utf-8 -*-

from rest_framework import generics, response
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404

from practics.models import PrTest
from pages.models import Specialty
from practics.serializers import (PrTestListSerializer, PrTestDetailSerializer,
                                  AnswerButtonsSerializer)



class PrTestListAPIView(generics.ListAPIView):
    """API запрос для получения списка тестов"""

    serializer_class = PrTestListSerializer

    #NOTE: потом сделать везде!
    # @swagger_auto_schema(
    #     responses={
    #         200: PrTestListSerializer(many=True),
    #         400: "Bad Request",
    #         404: "Not Found",
    #     }
    # )
    # def get(self, request, *args, **kwargs):
    #     return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return PrTest.objects.all().order_by('priority')

class PrTestDetailAPIView(generics.RetrieveAPIView):
    queryset = PrTest.objects.all()
    serializer_class = PrTestDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data

        buttons = instance.buttons.all()
        buttons_serializer = AnswerButtonsSerializer(buttons, many=True)
        data['buttons'] = buttons_serializer.data

        return response.Response(data)


class PrTestListBySpecialty(generics.ListAPIView):
    serializer_class = PrTestListSerializer

    def get_queryset(self):
        specialty_id = self.kwargs['speciality']
        specialty = get_object_or_404(Specialty, id=specialty_id)
        queryset = PrTest.objects.filter(speciality=specialty)
        queryset = queryset.order_by('priority')
        return queryset
