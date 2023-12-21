# -*- coding: utf-8 -*-


from rest_framework import serializers
from pages.models import Drug

class DrugListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = ['id', 'name']

class DrutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'
