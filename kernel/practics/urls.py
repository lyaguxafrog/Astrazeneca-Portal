# -*- coding: utf-8 -*-


from django.urls import path
from rest_framework import views

from practics.views import PrTestListAPIView

urlpatterns = [
    path('practicum_tests/', PrTestListAPIView.as_view(),
         name='practicum-tests-list'),
]
