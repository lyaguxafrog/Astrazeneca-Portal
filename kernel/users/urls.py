# -*- coding: utf-8 -*-




from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users.views import (SaveContentView, GetSavedContentView, 
                    SignUpAPIView, SignInAPIView,
                    HandleSSORedirectAPIView, SaveTokensAPIView, UserRegistrationView)

schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('sso/signup/', SignUpAPIView.as_view(), name='signup'),
    path('sso/signin/', SignInAPIView.as_view(), name='signin'),
    path('sso/sso-redirect/', HandleSSORedirectAPIView.as_view(), name='sso-redirect'),
    # path('sso/save-tokens/', SaveTokensAPIView.as_view(), name='save-tokens'),

    path('create_user/', UserRegistrationView.as_view(), name='create_user'),

    path('save-content/', SaveContentView.as_view(), name='save-content-create'),
    path('save-content/get/<int:user_id>', GetSavedContentView.as_view(),
         name='get-saved-content')
]
