# -*- coding: utf-8 -*-

from pages.models import LastAdds
from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.apps import apps
from pages.models import Drug, Events, VideoLectures




class SearchSerializer(serializers.Serializer):
    title = serializers.SerializerMethodField()
    model = serializers.CharField()
    id = serializers.IntegerField()
    url = serializers.URLField(required=False)  # Make the URL field optional
    speciality = serializers.ListField(child=serializers.IntegerField(),
                                       required=False)

    def get_title(self, instance):
        model_name = instance['model']
        if model_name == 'drug':
            return instance.get('name', '')
        if model_name == 'event':
            return instance.get('name', '')
        if model_name == 'video_lecture':
            return instance.get('video_article', '')
        return ''

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        model_name = representation.get('model', '')
        try:
            if model_name == 'drug':
                model_class = Drug
            elif model_name == 'event':
                model_class = Events
            elif model_name == 'video_lecture':
                model_class = VideoLectures
            else:
                model_class = None

            if model_class:
                model_instance = model_class.objects.get(pk=representation.get('id'))

                if hasattr(model_instance, 'speciality'):
                    representation['speciality'] = [speciality.id for speciality in model_instance.speciality.all()]
        except ObjectDoesNotExist as e:
            print(f"Error: {e}")

        return representation

class LastAddsSerializer(serializers.ModelSerializer):
    content_type = serializers.CharField(source='content_type_name')
    id = serializers.IntegerField(source='object_id')
    title = serializers.CharField(source='content')
    class Meta:
        model = LastAdds
        fields = ['content_type',
                  'id',
                  'title',
                  'speciality'
                  ]
