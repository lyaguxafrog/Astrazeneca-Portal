# -*- coding: utf-8 -*-


from django.urls import path
from rest_framework import views

from practics.views import (PrTestListAPIView, PrTestDetailAPIView,
                            PracticumCreateView, get_practicums_by_speciality,
                            get_practicum_by_id, update_practicum, delete_practicum)
from practics.views.prtest import PrTestListBySpecialty

urlpatterns = [
     path('practicum_tests/', PrTestListAPIView.as_view(),
          name='practicum-tests-list'),

     path('practicum_tests/<int:pk>', PrTestDetailAPIView.as_view(),
          name='practicum-test-detail'),

     path('practicum_tests/speciality/<int:speciality>/',
          PrTestListBySpecialty.as_view(),
          name='practicum-tests-list-by-speciality-id'),

    path('practicum/create/', PracticumCreateView.as_view(),
         name='practicum_create'),

    path('practicum/speciality/<int:speciality_id>/', get_practicums_by_speciality, name='get_practicums_by_speciality'),
    path('practicum/<int:practicum_id>/', get_practicum_by_id, name='get_practicum_by_id'),
    path('practicum/delete/<int:practicum_id>/', delete_practicum, name='delete_practicum'),
    path('practicum/update/<int:practicum_id>/', update_practicum, name='update_practicum'),

]
