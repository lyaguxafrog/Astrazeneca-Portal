# -*- coding: utf-8 -*-


from rest_framework import serializers
from pages.models import Events

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'
