# -*- coding: utf-8 -*-


from django.urls import path
from .views import (StoryListAPIView, StoryDetailAPIView, ArticlesDetailAPIView,
                    ArticlesListAPIView, DrugListAPIView,
                    DrugDetailAPIView, EventsListAPIView, EventsDetailAPIView,
                    VideoLecturesList, VideoLecturesDetail)

urlpatterns = [
    path('stories/<str:name>', StoryListAPIView.as_view(),
         name='story-list'),

    path('story/<int:id>', StoryDetailAPIView.as_view(),
         name='stories'),

    path('article/<str:name>', ArticlesListAPIView.as_view(),
         name='articles-list'),

    path('article/<int:pk>/', ArticlesDetailAPIView.as_view(),
         name='articles-detail'),

    path('drugs/', DrugListAPIView.as_view(), name='drugs-list'),

    path('drugs/<int:pk>/', DrugDetailAPIView.as_view(), name='drugs-detail'),

    path('events/', EventsListAPIView.as_view(), name='events-list'),

    path('events/<int:pk>/', EventsDetailAPIView.as_view(),
         name='events-detail'),

    path('video-lectures/<str:name>', VideoLecturesList.as_view(),
         name='video-lectures-list'),

    path('video-lectures/<int:pk>/', VideoLecturesDetail.as_view(),
         name='video-lectures-detail'),
]
