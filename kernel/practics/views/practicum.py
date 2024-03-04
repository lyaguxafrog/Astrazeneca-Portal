# -*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from practics.serializers import PracticumSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
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

@api_view(['GET'])
def get_practicums_by_speciality(request, speciality_id):
    practicums = Practicum.objects.filter(speciality_id=speciality_id)
    serializer = PracticumSerializer(practicums, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_practicum_by_id(request, practicum_id):
    try:
        practicum = Practicum.objects.get(id=practicum_id)
    except Practicum.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PracticumSerializer(practicum)
    return Response(serializer.data)

@api_view(['PUT'])
@swagger_auto_schema(
    request_body=PracticumSerializer,
    responses={
        200: PracticumSerializer,
        400: 'Bad Request',
        404: 'Not Found'
    },
    operation_description="Update a practicum",
    operation_id="update_practicum",
    tags=["Practicum"]
)
def update_practicum(request, practicum_id):
    try:
        practicum = Practicum.objects.get(id=practicum_id)
    except Practicum.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PracticumSerializer(practicum, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_practicum(request, practicum_id):
    try:
        practicum = Practicum.objects.get(id=practicum_id)
        practicum.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Practicum.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
