# -*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from practics.serializers import PracticumSerializer
from drf_yasg.utils import swagger_auto_schema


class PracticumCreateView(APIView):
    @swagger_auto_schema(
        request_body=PracticumSerializer,
        responses={
            201: PracticumSerializer,
            400: 'Bad Request'
        },
        operation_description="Create a new practicum",
        operation_id="create_practicum",
        tags=["Practicum"]
    )
    def post(self, request, *args, **kwargs):
        serializer = PracticumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
