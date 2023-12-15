# -*- coding: utf-8 -*-

from django.urls import path
from pages.views import (
    StoryListView,
    StoryCreateView,
    StoryUpdateView,
    StoryDeleteView,
    StoryDetailView,
)

urlpatterns = [
    path('', StoryListView.as_view(), name='story-list-view'),
    path('create/', StoryCreateView.as_view(), name='story-create-view'),
    path('<int:pk>/', StoryUpdateView.as_view(), name='story-update-view'),
    path('<int:pk>/delete/', StoryDeleteView.as_view(), name='story-delete-view'),
    path('detail/<int:pk>/', StoryDetailView.as_view(), name='story-detail-view'),
]
