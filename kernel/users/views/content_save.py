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
        request_body=ContentSaveSerializer,
        responses={201: 'Content saved successfully'},
    )
    def post(self, request, *args, **kwargs):
        serializer = ContentSaveSerializer(data=request.data)
        if serializer.is_valid():
            user_profile = UserProfile.objects.get(user=request.user)
            content_type = serializer.validated_data.get("content_type")
            content_id = serializer.validated_data.get("content_id")
            user_profile.saved_content[content_type] = content_id
            user_profile.save()
            return Response({"message": f"Content {content_id} saved successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetSavedContentView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={200: 'Success'},
    )
    def get(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        saved_content = user_profile.saved_content
        return Response(saved_content, status=status.HTTP_200_OK)