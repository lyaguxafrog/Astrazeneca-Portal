# -*- coding: utf-8 -*-


from django.urls import path
from .views import (StoryListAPIView, StoryDetailAPIView,
                    ArticleDetailAPIView, DrugListAPIView,
                    DrugDetailAPIView, EventsAPIView, ArticlesBySpecialtyAPIView,
                    VideoLecturesList, VideoLecturesDetail, SpecialtyListAPIView)

urlpatterns = [

    path('specialty', SpecialtyListAPIView.as_view(),
         name='specialty'),

     path('articles/specialty/<int:specialty_id>/',
          ArticlesBySpecialtyAPIView.as_view(), name='articles_by_specialty'),

    path('stories/<str:name>', StoryListAPIView.as_view(),
         name='story-list'),

    path('story/<int:id>', StoryDetailAPIView.as_view(),
         name='stories'),

    path('articles/<int:id>', ArticleDetailAPIView.as_view(),
         name='article'),


    path('drugs/', DrugListAPIView.as_view(), name='drugs-list'),

    path('drugs/<int:pk>/', DrugDetailAPIView.as_view(), name='drugs-detail'),

    path('events/', EventsAPIView.as_view(), name='events-list'),

    path('video-lectures/<str:name>', VideoLecturesList.as_view(),
         name='video-lectures-list'),

    path('video-lectures/<int:pk>/', VideoLecturesDetail.as_view(),
         name='video-lectures-detail'),
]
