# -*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pages.models import MainPageApproveNumber
from pages.serializers import MainPageApproveNumberSerializer

class MainPageApproveNumberAPIView(APIView):
    def get(self, request, *args, **kwargs):
        main_page_number = MainPageApproveNumber.objects.first()

        if main_page_number:
            serializer = MainPageApproveNumberSerializer(main_page_number)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
