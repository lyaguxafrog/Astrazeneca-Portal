# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import UserProfile
from users.serializers import ContentSaveSerializer
from drf_yasg.utils import swagger_auto_schema


class SaveContentView(APIView):
    permission_classes = [IsAuthenticated]


    @swagger_auto_schema(
    request_body=ContentSaveSerializer,  # Добавьте эту строку
    responses={201: 'Content saved successfully'},
)

    def post(self, request, *args, **kwargs):
        serializer = ContentSaveSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data.get("user_id")
            content_type = serializer.validated_data.get("content_type")
            content_id = serializer.validated_data.get("content_id")

            user_profile = UserProfile.objects.get(user_id=user_id)
            user_profile.save_content(content_type, content_id)

            return Response({"message": f"Content {content_id} saved successfully"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
