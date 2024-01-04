from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import UserProfile
from pages.models import Articles, Drug, Events, VideoLectures
from users.serializers import (ContentSaveSerializer, ArticleSerializer,
                               DrugSerializer, VideoLecturesSerializer,
                               EventsSerializer, GetSavedContentViewSerializer,
                               ContentRemoveSerializer)
from users.serializers.save_content import UserProfileSerializer

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
            try:
                user_profile = UserProfile.objects.get(id=user_id)
                content_type = serializer.validated_data.get("content_type")
                content_id = serializer.validated_data.get("content_id")

                # Получаем текущий сохраненный контент
                saved_content = user_profile.saved_content.get(content_type, [])
                # Добавляем новый контент
                saved_content.append(content_id)
                # Присваиваем обновленный контент обратно
                user_profile.saved_content[content_type] = saved_content

                user_profile.save()
                return Response({"message": f"Контент {content_id} успешно сохранен"}, status=status.HTTP_201_CREATED)
            except UserProfile.DoesNotExist:
                return Response({"message": "Профиль пользователя не найден"}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetSavedContentView(generics.RetrieveAPIView):
    serializer_class = GetSavedContentViewSerializer

    def get_object(self):
        user_profile = UserProfile.objects.get(id=self.kwargs['user_id'])
        saved_content = user_profile.saved_content
        serialized_content = {}

        for content_type, content_ids in saved_content.items():
            if content_type == 'article':
                articles = Articles.objects.filter(id__in=content_ids)
                serialized_content['article'] = ArticleSerializer(articles, many=True).data
            elif content_type == 'video':
                video_lectures = VideoLectures.objects.filter(id__in=content_ids)
                serialized_content['video'] = VideoLecturesSerializer(video_lectures, many=True).data
            elif content_type == 'drug':
                drugs = Drug.objects.filter(id__in=content_ids)
                serialized_content['drug'] = DrugSerializer(drugs, many=True).data
            elif content_type == 'event':
                events = Events.objects.filter(id__in=content_ids)
                serialized_content['event'] = EventsSerializer(events, many=True).data

        return {
            "message": "Успех",
            "saved_content": serialized_content,
        }



class RemoveContentView(generics.DestroyAPIView):
    serializer_class = ContentRemoveSerializer

    @swagger_auto_schema(
        request_body=ContentRemoveSerializer,
        responses={204: 'Content removed successfully'},
    )
    def delete(self, request, *args, **kwargs):
        serializer = ContentRemoveSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data.get("user_id")
            content_type = serializer.validated_data.get("content_type")
            content_id = serializer.validated_data.get("content_id")

            try:
                user_profile = UserProfile.objects.get(id=user_id)

                # Remove content from the saved_content dictionary
                saved_content = user_profile.saved_content.get(content_type, [])
                if content_id in saved_content:
                    saved_content.remove(content_id)
                    user_profile.saved_content[content_type] = saved_content
                    user_profile.save()

                    return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response({"message": f"Content {content_id} not found in favorites"},
                                    status=status.HTTP_404_NOT_FOUND)

            except UserProfile.DoesNotExist:
                return Response({"message": "User profile not found"}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
