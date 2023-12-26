# -*- coding: utf-8 -*-




from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import SsoRegistrationLink, SsoLoginLink, SsoCallbackView, SaveContentView

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
    path('sso/registration-link/', SsoRegistrationLink.as_view(), name='sso-registration-link'),
    path('sso/login-link/', SsoLoginLink.as_view(), name='sso-login-link'),
    path('sso/callback/', SsoCallbackView.as_view(), name='sso-callback'),
    path('save-content/', SaveContentView.as_view(), name='save-content-create'),

]
