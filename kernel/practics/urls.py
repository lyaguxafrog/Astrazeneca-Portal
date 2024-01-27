# -*- coding: utf-8 -*-


from django.urls import path
from rest_framework import views

from practics.views import (PrTestListAPIView, PrTestDetailAPIView,
                            PracticumDetailView, PracticumListView,
                            PracticumListBySpecialty)

urlpatterns = [
     path('practicum_tests/', PrTestListAPIView.as_view(),
          name='practicum-tests-list'),
     path('practicum_tests/<int:pk>', PrTestDetailAPIView.as_view(),
          name='practicum-test-detail'),
     path('practicum/<int:pk>/', PracticumDetailView.as_view(),
          name='practicum-detail'),
     path('practicum/speciality/<int:speciality>/', PracticumListBySpecialty.as_view(),
          name='practicum-list-by-speciality-id' ),
     path('practicum/', PracticumListView.as_view(),
          name='practicum-list')
]
