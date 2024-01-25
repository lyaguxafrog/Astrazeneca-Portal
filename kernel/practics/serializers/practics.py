# -*- coding: utf-8 -*-

from rest_framework import serializers
from urllib.parse import urlparse

from practics.models import (Practicum, Screens, ScreenPopupBlock,
                             ScreenButton, ScreenImageBlock, ScreenTextBlock)


class TextBlockSerializer(serializers.ModelSerializer):
    """ Текстовый блок в экранах """
    class Meta:
        model = ScreenTextBlock
        fields = ['__all__']
