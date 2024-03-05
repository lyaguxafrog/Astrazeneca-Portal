# -*- coding: utf-8 -*-


from django.urls import path

from practics.views import (PrTestListAPIView, PrTestDetailAPIView,
                            PracticumCreateView, GetPracticumsBySpecialityView,
                            GetPracticumByIdView, DeletePracticumView,
                            UpdatePracticumView)
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

    path('practicum/speciality/<int:speciality_id>/', GetPracticumsBySpecialityView.as_view(), name='get_practicums_by_speciality'),
    path('practicum/<int:practicum_id>/', GetPracticumByIdView.as_view(), name='get_practicum_by_id'),
    path('practicum/delete/<int:practicum_id>/', DeletePracticumView.as_view(), name='delete_practicum'),
    path('practicum/update/<int:practicum_id>/', UpdatePracticumView.as_view(), name='update_practicum'),

]
