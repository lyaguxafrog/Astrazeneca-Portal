from rest_framework import serializers
from users.models import UserProfile
from pages.models import Specialty

class UserProfileSerializer(serializers.ModelSerializer):
    specialty = serializers.PrimaryKeyRelatedField(
        queryset=Specialty.objects.all()
    )

    class Meta:
        model = UserProfile
        fields = ['temporary_token', 'specialty']
