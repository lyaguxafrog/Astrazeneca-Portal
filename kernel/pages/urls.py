# -*- coding: utf-8 -*-


from django.urls import path
from .views import StoryListAPIView, ArticlesDetailAPIView, ArticlesListAPIView

urlpatterns = [
    path('stories/', StoryListAPIView.as_view(), name='story-list'),
    path('articles/', ArticlesListAPIView.as_view(), name='articles-list'),
    path('articles/<int:pk>/', ArticlesDetailAPIView.as_view(), name='articles-detail'),
    # Добавьте другие URL-пути, если необходимо
]
