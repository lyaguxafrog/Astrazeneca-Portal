# -*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from practics.serializers import PracticumSerializer
from drf_yasg.utils import swagger_auto_schema
from practics.models import Practicum



class PracticumCreateView(APIView):
    @swagger_auto_schema(
        request_body=PracticumSerializer,
        responses={
            201: PracticumSerializer,
            400: 'Bad Request'
        },
        operation_description="Create a new practicum",
        operation_id="create_practicum",
        tags=["practicum"]
    )
    def post(self, request, *args, **kwargs):
        serializer = PracticumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetPracticumsBySpecialityView(APIView):
    @swagger_auto_schema(
        responses={
            200: PracticumSerializer(many=True),
            404: 'Not Found'
        }
    )
    def get(self, request, speciality_id):
        practicums = Practicum.objects.filter(speciality_id=speciality_id)
        serializer = PracticumSerializer(practicums, many=True)
        return Response(serializer.data)

class GetPracticumByIdView(APIView):
    @swagger_auto_schema(
        responses={
            200: PracticumSerializer,
            404: 'Not Found'
        }
    )
    def get(self, request, practicum_id):
        try:
            practicum = Practicum.objects.get(id=practicum_id)
        except Practicum.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PracticumSerializer(practicum)
        return Response(serializer.data)


class UpdatePracticumView(APIView):
    @swagger_auto_schema(
        request_body=PracticumSerializer,
        responses={
            200: PracticumSerializer,
            400: 'Bad Request',
            404: 'Not Found'
        }
    )
    def put(self, request, practicum_id):
        try:
            practicum = Practicum.objects.get(id=practicum_id)
        except Practicum.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PracticumSerializer(practicum, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeletePracticumView(APIView):
    @swagger_auto_schema(
        responses={
            204: 'No Content',
            404: 'Not Found'
        }
    )
    def delete(self, request, practicum_id):
        try:
            practicum = Practicum.objects.get(id=practicum_id)
            practicum.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Practicum.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class GetAllPracticumsView(APIView):
    @swagger_auto_schema(
        responses={
            200: PracticumSerializer(many=True),
            404: 'Not Found'
        }
    )
    def get(self, request, *args, **kwargs):
        practicums = Practicum.objects.all()
        serializer = PracticumSerializer(practicums, many=True)
        return Response(serializer.data)
