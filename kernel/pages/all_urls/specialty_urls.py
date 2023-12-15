from django.urls import path
from pages.views import (
    SpecialtyCreateView,
    SpecialtyUpdateView,
    SpecialtyDeleteView,
    SpecialtyListView,
    SpecialtyDetailView,
)

urlpatterns = [
    path('create/', SpecialtyCreateView.as_view(),
         name='specialty-create-view'),

    path('<int:pk>/', SpecialtyUpdateView.as_view(),
         name='specialty-update-view'),

    path('<int:pk>/delete/', SpecialtyDeleteView.as_view(),
         name='specialty-delete-view'),

    path('list/', SpecialtyListView.as_view(),
         name='specialty-list-view'),

    path('detail/<int:pk>/', SpecialtyDetailView.as_view(),
         name='specialty-detail-view'),
]
