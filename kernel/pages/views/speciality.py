# -*- coding: utf-8 -*-


from rest_framework import generics
from pages.models import Specialty
from pages.serializers import SpecialtySerializer

class SpecialtyListAPIView(generics.ListAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
