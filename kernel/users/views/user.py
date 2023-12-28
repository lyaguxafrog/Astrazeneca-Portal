# -*- coding: utf-8 0*0

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import UserProfile
from users.serializers import UserProfileSerializer
from drf_yasg.utils import swagger_auto_schema



class CreateUserAPIView(APIView):
    @swagger_auto_schema(request_body=UserProfileSerializer)
    def post(self, request, format=None):
        serializer = UserProfileSerializer(data=request.data)

        if serializer.is_valid():
            # Assuming 'temporary_token' and 'specialty' are provided in the request data
            temporary_token = serializer.validated_data['temporary_token']
            specialty = serializer.validated_data['specialty']

            # Assuming you have a function to generate a User and UserProfile
            user_profile = create_user_with_profile(temporary_token, specialty)

            return Response(UserProfileSerializer(user_profile).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def create_user_with_profile(temporary_token, specialty):
    # Assuming you have a function to create a User and UserProfile
    user = User.objects.create(username=f'user_{temporary_token}')
    user.set_unusable_password()
    user.save()

    user_profile = UserProfile.objects.create(user=user, temporary_token=temporary_token, specialty=specialty)
    return user_profile
