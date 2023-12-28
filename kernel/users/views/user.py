# -*- coding: utf-8 0*0


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from pages.models import Specialty
from users.models import UserProfile
from users.serializers import UserProfileSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



class CreateUserAPIView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'temporary_token': openapi.Schema(type=openapi.TYPE_STRING),
                'specialty': openapi.Schema(type=openapi.TYPE_OBJECT, properties={'id': openapi.Schema(type=openapi.TYPE_INTEGER)})
            },
            required=['temporary_token', 'specialty']
        ),
        responses={200: 'Success'}
    )
    def post(self, request, *args, **kwargs):
        temporary_token = request.data.get('temporary_token')
        specialty_id = request.data.get('specialty', {}).get('id')

        if not specialty_id:
            return Response({'error': 'Specialty ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            specialty = Specialty.objects.get(id=specialty_id)
        except Specialty.DoesNotExist:
            return Response({'error': 'Specialty not found'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserProfileSerializer(data={'temporary_token': temporary_token, 'specialty': {'id': specialty_id}})

        if serializer.is_valid():  
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
