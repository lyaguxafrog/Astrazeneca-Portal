# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from pages.models import Specialty

from practics.models import Practicum
from practics.serializers.practics import (PracticumSerializer,
                                           PracticumListSerializer)

class PracticumDetailView(APIView):
    def get(self, request, pk, format=None):
        try:
            practicum = Practicum.objects.get(pk=pk)
        except Practicum.DoesNotExist:
            return Response({"error": "Practicum not found"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = PracticumSerializer(practicum)
        return Response(serializer.data)

class PracticumListView(generics.ListAPIView):
    serializer_class = PracticumListSerializer

    def get_queryset(self):
        return Practicum.objects.all().order_by('priority')


class PracticumListBySpecialty(generics.ListAPIView):
    serializer_class = PracticumListSerializer

    def get_queryset(self):
        specialty_id = self.kwargs['speciality']
        specialty = get_object_or_404(Specialty, id=specialty_id)
        queryset = Practicum.objects.filter(speciality=specialty)
        queryset = queryset.order_by('priority')
        return queryset
