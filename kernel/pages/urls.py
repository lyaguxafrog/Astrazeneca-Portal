# -*- coding: utf-8 -*-


from django.urls import path
from .views import (StoryListAPIView, StoryDetailAPIView, ArticlesDetailAPIView,
                    ArticlesListAPIView, DrugListAPIView,
                    DrugDetailAPIView, EventsAPIView,
                    VideoLecturesList, VideoLecturesDetail, SpecialtyListAPIView)

urlpatterns = [

    path('specialty', SpecialtyListAPIView.as_view(),
         name='specialty'),

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

    path('events/', EventsAPIView.as_view(), name='events-list'),

    path('video-lectures/<str:name>', VideoLecturesList.as_view(),
         name='video-lectures-list'),

    path('video-lectures/<int:pk>/', VideoLecturesDetail.as_view(),
         name='video-lectures-detail'),
]
