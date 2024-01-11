# -*- coding: utf-8 -*-

from pages.models import LastAdds
from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.apps import apps



class SearchSerializer(serializers.Serializer):
    title = serializers.SerializerMethodField()
    model = serializers.CharField()
    id = serializers.IntegerField()
    url = serializers.URLField(required=False)  # Make the URL field optional
    speciality = serializers.ListField(child=serializers.IntegerField(), required=False)


    def get_title(self, instance):
        model_name = instance['model']
        # if model_name == 'article':
        #     return instance.get('article_name', '')
        # if model_name == 'content_block':
        #     return instance.get('text', '')
        if model_name == 'drug':
            return instance.get('name', '')
        # elif model_name == 'drug_faq':
        #     return instance.get('title', '')
        elif model_name == 'event':
            return instance.get('name', '')
        elif model_name == 'video_lecture':
            return instance.get('video_article', '')
        return ''

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        model_name = representation.get('model', '')
        if model_name and model_name != 'event':
            try:
                model_class = apps.get_model(app_label='pages', model_name=model_name)
                model_instance = model_class.objects.get(pk=representation.get('id'))
                representation['speciality'] = [specialty.id for specialty in model_instance.speciality.all()]
            except (LookupError, ObjectDoesNotExist):
                # Handle the case when the model or instance is not found
                pass

        return representation

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
