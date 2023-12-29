# -*- coding: utf-8 -*-


from rest_framework import serializers
from pages.models import MainPageApproveNumber

class MainPageApproveNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageApproveNumber
        fields = ['number']
