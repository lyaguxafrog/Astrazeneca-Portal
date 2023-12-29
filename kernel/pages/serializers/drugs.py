# -*- coding: utf-8 -*-


from rest_framework import serializers
from pages.models import Drug, Icon, DrugFAQ


class DrugListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Drug
        fields = ['id', 'name', 'brief_info', 'image']

    def get_image(self, obj):
        return obj.image.url if obj.image else None

class IconSerializer(serializers.ModelSerializer):
    image_file = serializers.SerializerMethodField()

    class Meta:
        model = Icon
        fields = ['id', 'image_file']

    def get_image_file(self, obj):
        return obj.image_file.url if obj.image_file else None

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugFAQ
        fields = ['title',
                  'text',
                  'order']


class DrugSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    icons = IconSerializer(many=True, read_only=True)
    faq = FAQSerializer(many=True, read_only=True)

    class Meta:
        model = Drug
        fields = '__all__'

    def get_image(self, obj):
        return obj.image.url if obj.image else None
