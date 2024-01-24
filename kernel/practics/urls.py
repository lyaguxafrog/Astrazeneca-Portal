# -*- coding: utf-8 -*-


from django.urls import path
from rest_framework import views

from practics.views import PrTestListAPIView, PrTestDetailAPIView

urlpatterns = [
    path('practicum_tests/', PrTestListAPIView.as_view(),
         name='practicum-tests-list'),
    path('practicum_tests/<int:pk>', PrTestDetailAPIView.as_view(),
         name='practicum-test-detail'),
]
