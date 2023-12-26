# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import UserProfile
from users.serializers import ContentSaveSerializer
from drf_yasg.utils import swagger_auto_schema


class SaveContentView(APIView):
    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=ContentSaveSerializer,
        responses={201: 'Content saved successfully'},
    )
    def post(self, request, *args, **kwargs):
        serializer = ContentSaveSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data.get("user_id")
            content_type = serializer.validated_data.get("content_type")
            content_id = serializer.validated_data.get("content_id")

            # Попробуйте получить профиль пользователя или создать новый, если его нет
            user_profile, created = UserProfile.objects.get_or_create(user_id=user_id)

            # Теперь у вас есть профиль пользователя, и вы можете выполнять операции с ним
            user_profile.save_content(content_type, content_id)

            return Response({"message": f"Content {content_id} saved successfully"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetSavedContentView(APIView):
    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={200: 'Success'},
    )
    def get(self, request, user_id, *args, **kwargs):
        try:
            user_profile = UserProfile.objects.get(user_id=user_id)
            saved_content = user_profile.saved_content
            return Response(saved_content, status=status.HTTP_200_OK)
        except UserProfile.DoesNotExist:
            return Response({"message": f"UserProfile with user_id {user_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
