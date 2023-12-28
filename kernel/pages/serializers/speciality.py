# -*- coding: utf-8 -*-


from rest_framework import serializers
from pages.models import Specialty

class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'
        ref_name = 'PagesSpecialty'  # Set a unique ref_name
