# config/urls.py
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView


schema_view = get_schema_view(
    openapi.Info(
        title="Portal API",
        default_version='v1',
        description="API для серсиса",
        terms_of_service="",
        contact=openapi.Contact(url='https://github.com/lyaguxafrog'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('pages.urls')),
    path('api/', include('practics.urls')),
    path('api/', include('users.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('author', RedirectView.as_view(url='https://github.com/lyaguxafrog'), name='github-redirect'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from config.settings import DOCS
if DOCS:
    urlpatterns += [
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
        ]
