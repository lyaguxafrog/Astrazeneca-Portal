# -*- coding: utf-8 -*-


from rest_framework import serializers
from pages.models import Events

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Update the 'cover' field to contain the relative path
        representation['cover'] = instance.cover.url if instance.cover else None
        return representation
