# -*- coding: utf-8 -*-

from rest_framework import serializers

class SearchResultsSerializer(serializers.Serializer):
    model = serializers.CharField()
    id = serializers.IntegerField()
    text = serializers.CharField()
