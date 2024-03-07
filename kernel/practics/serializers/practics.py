# -*- coding: utf-8 -*-

from rest_framework import serializers

from practics.models import (Practicum, Screens, ScreenButton, ScreenImageBlock,
                             ScreenPopupBlock, ScreenTextBlock, PopUpPoint)
from pages.models import Specialty


class ScreenTextBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenTextBlock
        fields = [
            'id',
            'screen_id',
            'side',
            'text',
            'order'
        ]
        extra_kwargs = {
            'screen': {'required': False},
        }

class ScreenImageBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenImageBlock
        fields = [
            'id',
            'screen_id',
            'order',
            'side',
            'image',
            'image_desktop_810px',
            'image_desktop_1620px',
            'image_mobile_400px',
            'image_mobile_800px'
        ]
        extra_kwargs = {
            'screen': {'required': False},
        }

class PopUpPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopUpPoint
        fields = '__all__'


class ScreenPopupBlockSerializer(serializers.ModelSerializer):
    popup_points = PopUpPointSerializer(many=True)

    class Meta:
        model = ScreenPopupBlock
        fields = '__all__'
        extra_kwargs = {
            'screen': {'required': False},
        }


class ScreenButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenButton
        fields = '__all__'
        extra_kwargs = {
            'screen': {'required': False},
        }

class ScreensSerializer(serializers.ModelSerializer):
    screen_text_block = ScreenTextBlockSerializer(many=True, required=False)
    screen_image_block = ScreenImageBlockSerializer(many=True, required=False)
    screen_popup_block = ScreenPopupBlockSerializer(many=True, required=False)
    screen_button_block = ScreenButtonSerializer(many=True, required=False)
    literature = serializers.CharField()
    leterature_approvals_and_decodings = serializers.CharField()
    approvals_and_decodings = serializers.CharField()

    class Meta:
        model = Screens
        fields = [
            'id',
            'screen_text_block',
            'screen_image_block',
            'screen_popup_block',
            'screen_button_block',
            'literature',
            'leterature_approvals_and_decodings',
            'approvals_and_decodings',
            'practicum',
        ]
        extra_kwargs = {
            'practicum': {'required': False},
        }

    def create(self, validated_data):
        screen_text_block_data = validated_data.pop('screen_text_block')
        screen_image_block_data = validated_data.pop('screen_image_block')
        screen_popup_block_data = validated_data.pop('screen_popup_block')
        screen_button_block_data = validated_data.pop('screen_button_block')
        screen_literature = validated_data.pop('literature')
        screen_leterature_approvals_and_decodings = validated_data.pop('leterature_approvals_and_decodings'),
        screen_approvals_and_decodings = validated_data.pop('approvals_and_decodings')

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
    screens = ScreensSerializer(many=True, required=False)

    class Meta:
        model = Practicum
        fields = [
            'id',
            'title',
            'description',
            'pacient_description',
            'speciality',
            'image',
            'priority',
            'screens',
            ]
        extra_kwargs = {
            'image': {'required': False},
        }

    def create(self, validated_data):
        screens_data = validated_data.pop('screens', [])
        speciality_data = validated_data.pop('speciality', [])
        practicum = Practicum.objects.create(**validated_data)

        for speciality_item in speciality_data:
            if isinstance(speciality_item, Specialty):
                practicum.speciality.add(speciality_item)
            else:
                speciality = Specialty.objects.get(id=speciality_item)
                practicum.speciality.add(speciality)

        for screen_data in screens_data:
            screen = Screens.objects.create(practicum=practicum, **screen_data)

            if 'screen_text_block' in screen_data:
                for text_block_data in screen_data['screen_text_block']:
                    ScreenTextBlock.objects.create(screen=screen, **text_block_data)

            if 'screen_image_block' in screen_data:
                for image_block_data in screen_data['screen_image_block']:
                    ScreenImageBlock.objects.create(screen=screen, **image_block_data)

            if 'screen_popup_block' in screen_data:
                for popup_block_data in screen_data['screen_popup_block']:
                    ScreenPopupBlock.objects.create(screen=screen, **popup_block_data)

            if 'screen_button_block' in screen_data:
                for button_block_data in screen_data['screen_button_block']:
                    ScreenButton.objects.create(screen=screen, **button_block_data)



        return practicum

    def update(self, instance, validated_data):
        # Проверяем, была ли предоставлена новая картинка
        image = validated_data.get('image', None)
        screens_data = validated_data.pop('screens', [])
        speciality_data = validated_data.pop('speciality', [])
        instance.speciality.set(speciality_data)


        for screen_data in screens_data:
            screen_id = screen_data.get('id')
            if screen_id:
                # Если экран существует, обновляем его
                screen = instance.screens.filter(id=screen_id).first()
                if screen:
                    for attr, value in screen_data.items():
                        setattr(screen, attr, value)
                    screen.save()
            else:
                # Если экран не существует, создаем новый
                Screens.objects.create(practicum=instance, **screen_data)


        if image is not None:
            # Если картинка была предоставлена, обновляем её
            instance.image = image

        # Обновляем остальные поля
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.pacient_description = validated_data.get('pacient_description', instance.pacient_description)
        instance.priority = validated_data.get('priority', instance.priority) # Добавлено обновление поля priority

        instance.save()
        return instance
