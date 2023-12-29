# -*- coding: utf-8 0*0

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from pages.models import Specialty
from users.models import UserProfile
from users.serializers import UserProfileSerializer

class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        if 'temporary_token' in request.data:
            try:
                user_profile = UserProfile.objects.get(temporary_token=request.data['temporary_token'])
                return Response({'user_id': user_profile.id}, status=status.HTTP_200_OK)
            except UserProfile.DoesNotExist:
                return Response("User profile not found", status=status.HTTP_404_NOT_FOUND)
        
        if 'specialty_id' in request.data:
            try:
                specialty = Specialty.objects.get(id=request.data['specialty_id'])
                serializer = UserProfileSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.validated_data['specialty'] = specialty  # Добавим специальность к данным перед сохранением
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Specialty.DoesNotExist:
                return Response("Specialty not found", status=status.HTTP_404_NOT_FOUND)

        return Response("Invalid request data", status=status.HTTP_400_BAD_REQUEST)
