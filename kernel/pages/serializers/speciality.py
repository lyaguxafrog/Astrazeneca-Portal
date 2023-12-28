# -*- coding: utf-8 -*-


from rest_framework import serializers
from pages.models import Specialty

class SpecialtySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Specialty
        fields = ['id', 'name', 'image_url', 'pro']

    def get_image_url(self, obj):
        if obj.image:
            return f"/media/{obj.image.name}"
        return None
