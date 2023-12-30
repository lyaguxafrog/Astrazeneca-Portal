from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import UserProfile
from pages.models import Specialty
from users.serializers import UserProfileSerializer



class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        temporary_token = request.data.get('temporary_token')
        existing_user_profile = UserProfile.objects.filter(temporary_token=temporary_token).first()

        if existing_user_profile:
            return Response({'user_id': existing_user_profile.id}, status=status.HTTP_200_OK)
        else:
            serializer = UserProfileSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'user_id': serializer.instance.id}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def handle_temporary_token(self, temporary_token):
        try:
            user_profile = UserProfile.objects.get(temporary_token=temporary_token)
            return Response({'user_id': user_profile.id}, status=status.HTTP_200_OK)
        except UserProfile.DoesNotExist:
            serializer = UserProfileSerializer(data={'temporary_token': temporary_token})
            if serializer.is_valid():
                serializer.save()
                return Response({'user_id': serializer.instance.id}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def handle_specialty_id(self, specialty_id, data):
        try:
            specialty = Specialty.objects.get(id=specialty_id)
            data['specialty'] = specialty.id
            serializer = UserProfileSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Specialty.DoesNotExist:
            return Response("Specialty not found", status=status.HTTP_404_NOT_FOUND)
