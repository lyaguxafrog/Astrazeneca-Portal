# -*- coding: utf-8 -*-

from rest_framework import serializers
from pages.serializers import SpecialtySerializer as PagesSpecialtySerializer
from pages.models import Specialty
from users.models import UserProfile

class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ['id']
        ref_name = 'UserSpecialty'  # Set a unique ref_name


class UserProfileSerializer(serializers.ModelSerializer):
    specialty = SpecialtySerializer()

    class Meta:
        model = UserProfile
        fields = ['temporary_token', 'saved_content', 'specialty']

    def create(self, validated_data):
        # Проверяем наличие 'specialty' в данных
        if 'specialty' in validated_data:
            # Извлекаем 'id' из 'specialty'
            specialty_data = validated_data.pop('specialty', None)

            # Проверяем наличие 'id' в 'specialty_data'
            if specialty_data and 'id' in specialty_data:
                specialty_id = specialty_data['id']

                try:
                    # Получаем экземпляр Specialty
                    specialty = Specialty.objects.get(id=specialty_id)

                    # Создаем экземпляр UserProfile с извлеченной специальностью
                    user_profile = UserProfile.objects.create(specialty=specialty, **validated_data)
                    return user_profile
                except Specialty.DoesNotExist:
                    raise serializers.ValidationError({'error': 'Specialty not found'})
            else:
                raise serializers.ValidationError({'error': 'Invalid specialty data'})
        else:
            raise serializers.ValidationError({'error': 'Specialty data missing'})
