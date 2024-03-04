# -*- coding: utf-8 -*-


from rest_framework import serializers

from practics.models import (Practicum, Screens, ScreenButton, ScreenImageBlock,
                             ScreenPopupBlock, ScreenTextBlock)



class ScreenTextBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenTextBlock
        fields = '__all__'

class ScreenImageBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenImageBlock
        fields = '__all__'

class ScreenPopupBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenPopupBlock
        fields = '__all__'

class ScreenButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenButton
        fields = '__all__'

class ScreensSerializer(serializers.ModelSerializer):
    screen_text_block = ScreenTextBlockSerializer(many=True)
    screen_image_block = ScreenImageBlockSerializer(many=True)
    screen_popup_block = ScreenPopupBlockSerializer(many=True)
    screen_button_block = ScreenButtonSerializer(many=True)

    class Meta:
        model = Screens
        fields = '__all__'

    def create(self, validated_data):
        screen_text_block_data = validated_data.pop('screen_text_block')
        screen_image_block_data = validated_data.pop('screen_image_block')
        screen_popup_block_data = validated_data.pop('screen_popup_block')
        screen_button_block_data = validated_data.pop('screen_button_block')
        screens = Screens.objects.create(**validated_data)

        for text_block_data in screen_text_block_data:
            ScreenTextBlock.objects.create(screen=screens, **text_block_data)

        for image_block_data in screen_image_block_data:
            ScreenImageBlock.objects.create(screen=screens, **image_block_data)

        for popup_block_data in screen_popup_block_data:
            ScreenPopupBlock.objects.create(screen=screens, **popup_block_data)

        for button_block_data in screen_button_block_data:
            ScreenButton.objects.create(screen=screens, **button_block_data)

        return screens

class PracticumSerializer(serializers.ModelSerializer):
    screens = ScreensSerializer(many=True)

    class Meta:
        model = Practicum
        fields = '__all__'

    def create(self, validated_data):
        screens_data = validated_data.pop('screens')
        practicum = Practicum.objects.create(**validated_data)

        for screen_data in screens_data:
            ScreensSerializer().create(screen_data)

        return practicum
