# -*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from pages.models import Specialty, Story
from pages.serializers import (SpecialtySerializer,
        StoryCreateUpdateSerializer, StorySerializer)




class SpecialtyCreateView(APIView):
    def post(self, request):
        serializer = SpecialtySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpecialtyUpdateView(APIView):
    def put(self, request, pk):
        specialty = get_object_or_404(Specialty, pk=pk)
        serializer = SpecialtySerializer(specialty, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpecialtyDeleteView(APIView):
    def delete(self, request, pk):
        specialty = get_object_or_404(Specialty, pk=pk)
        specialty.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SpecialtyListView(APIView):
    def get(self, request):
        specialties = Specialty.objects.all()
        serializer = SpecialtySerializer(specialties, many=True)
        return Response(serializer.data)

class SpecialtyDetailView(APIView):
    def get(self, request, pk):
        specialty = get_object_or_404(Specialty, pk=pk)
        serializer = SpecialtySerializer(specialty)
        return Response(serializer.data)


class StoryCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = StoryCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoryUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        story = get_object_or_404(Story, pk=pk, author=request.user)
        serializer = StoryCreateUpdateSerializer(story, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StoryDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        story = get_object_or_404(Story, pk=pk, author=request.user)
        story.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StoryListView(APIView):
    def get(self, request):
        stories = Story.objects.all()
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data)


class StoryDetailView(APIView):
    def get(self, request, pk):
        story = get_object_or_404(Story, pk=pk)
        serializer = StorySerializer(story)
        return Response(serializer.data)
