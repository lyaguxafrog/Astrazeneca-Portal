from rest_framework import serializers
from users.models import UserProfile
from pages.models import Specialty

class UserProfileSerializer(serializers.ModelSerializer):
    specialty_id = serializers.PrimaryKeyRelatedField(
        queryset=Specialty.objects.all(), source='specialty', write_only=True)

    class Meta:
        model = UserProfile
        fields = ['temporary_token', 'specialty_id']

    def create(self, validated_data):
        specialty_id = validated_data.pop('specialty_id')
        specialty = Specialty.objects.get(id=specialty_id)
        user_profile = UserProfile.objects.create(specialty=specialty, **validated_data)
        return user_profile
