# -*- coding: utf-8 -*-

from jose import jwt
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.parsers import JSONParser
from drf_yasg.utils import swagger_auto_schema




from users.models import UserProfile
from users.serializers import UserProfileSerializer

from decouple import config

SECRET_KEY = config("SECRET_KEY")  # Замените на ваш секретный ключ
SSO_URL = config("SSO_URL")
source = config("OUR_DOMAIN")
next_url = config("OUR_DOMAIN")


class SignUpAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        sso_signup_url = f'{SSO_URL}/signup?source={source}&next_url={next_url}'
        return Response({'sso_signup_url': sso_signup_url})


class SignInAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        sso_signin_url = f'{SSO_URL}/signin?source={source}&next_url={next_url}'
        return Response({'sso_signin_url': sso_signin_url})


class HandleSSORedirectAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        access_token = request.GET.get('access_token', None)
        refresh_token = request.GET.get('refresh_token', None)
        status = request.GET.get('status', None)

        if status == '1' and access_token and refresh_token:
            # Успешная регистрация или авторизация
            # Декодируем access_token для получения данных
            try:
                decoded_token = jwt.decode(access_token, SECRET_KEY, algorithms='HS256')
                user_id = decoded_token.get('user_id')
            except jwt.ExpiredSignatureError:
                return Response({'error': 'Expired access token'})
            except jwt.JWTError:
                return Response({'error': 'Invalid access token'})

            # Создаем или получаем пользователя по user_id
            user, created = User.objects.get_or_create(username=f'sso_user_{user_id}')

            # Аутентифицируем пользователя
            user = authenticate(request, username=user.username)
            login(request, user)

            # Возвращает токены на фронтенд в JSON-формате
            return Response({'access_token': access_token, 'refresh_token': refresh_token})
        else:
            # Ошибка регистрации или авторизации
            return Response({'error': 'Registration or authorization error'})


class SaveTokensAPIView(APIView):
    authentication_classes = []  # Disable authentication
    permission_classes = []  # Disable permission checks
    parser_classes = [JSONParser]  # Specify JSONParser for parsing JSON data


    @swagger_auto_schema(
    request_body=UserProfileSerializer,
    responses={201: 'Tokes saved successfully'},
    )

    def post(self, request, *args, **kwargs):
        data = request.data

        # Валидация данных и создание/обновление объекта UserProfile
        serializer = UserProfileSerializer(data=data)
        if serializer.is_valid():
            user = request.user if request.user.is_authenticated else None

            # Modify the following line to handle user when not authenticated
            user_profile, created = UserProfile.objects.get_or_create(user=user)
            user_profile.sso_user_id = serializer.validated_data.get('sso_user_id', None)
            user_profile.access_token = serializer.validated_data.get('access_token', None)
            user_profile.refresh_token = serializer.validated_data.get('refresh_token', None)
            user_profile.token_expiry = serializer.validated_data.get('token_expiry', None)
            user_profile.save()

            return Response({'message': 'Tokens saved successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
