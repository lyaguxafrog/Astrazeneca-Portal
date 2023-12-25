# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import SsoCallbackSerializer
from django.urls import reverse
from jose import jwt
from decouple import config


class SsoRegistrationLink(APIView):
    def get(self, request, *args, **kwargs):
        source = config('SSO_OUR_DOMAIN')
        next_url = config('SSO_REDIRECT_DOMAIN')

        registration_url = f"http://sso.azmost.ru/signup?source={source}&next_url={next_url}"

        return Response({"registration_link": registration_url})


class SsoLoginLink(APIView):
    def get(self, request, *args, **kwargs):
        source = config('SSO_OUR_DOMAIN')
        next_url = config('SSO_REDIRECT_DOMAIN')

        login_url = f"http://sso.azmost.ru/signin?source={source}&next_url={next_url}"

        return Response({"login_link": login_url})


class SsoCallbackView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = SsoCallbackSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        access_token = serializer.validated_data.get("access_token")
        refresh_token = serializer.validated_data.get("refresh_token")
        status = serializer.validated_data.get("status")

        if status == "1" and access_token and refresh_token:
            decoded_access_token = jwt.decode(access_token, config("SECRET_KEY"), algorithms=['HS256'])
            user_id = decoded_access_token.get("user_id")

            return Response({"message": "Tokens processed successfully"})
        else:
            return Response({"error": "Token processing failed"}, status=status.HTTP_400_BAD_REQUEST)
