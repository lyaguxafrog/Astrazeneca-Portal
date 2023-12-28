# -*- coding: utf-8 -*-


from django.urls import path
from rest_framework import views
from .views import (StoryListAPIView, StoryDetailAPIView,
                    ArticleDetailAPIView, DrugListAPIView,
                    SpecialityStoryListAPIView,
                    DrugDetailAPIView, EventsAPIView, ArticlesBySpecialtyAPIView,
                    VideoLecturesList, VideoLecturesDetail, SpecialtyListAPIView,
                    SearchResultsView)

urlpatterns = [

    path('specialty', SpecialtyListAPIView.as_view(),
         name='specialty'),

     path('articles/specialty/<int:specialty_id>/',
          ArticlesBySpecialtyAPIView.as_view(), name='articles_by_specialty'),

     path('stories/', StoryListAPIView.as_view(), name='story-list'),
     path('stories/<int:id>/', StoryDetailAPIView.as_view(), name='story-detail'),
     path('stories/speciality/<int:id>/',
          SpecialityStoryListAPIView.as_view(), name='story-list-by-speciality'),



    path('articles/<int:id>', ArticleDetailAPIView.as_view(),
         name='article'),

     path('search/', SearchResultsView.as_view({'get': 'list'}), name='search-results'),

    path('drugs/', DrugListAPIView.as_view(), name='drugs-list'),

    path('drugs/<int:pk>/', DrugDetailAPIView.as_view(), name='drugs-detail'),

    path('events/', EventsAPIView.as_view(), name='events-list'),

    path('video-lectures/speciality/<int:id>', VideoLecturesList.as_view(),
         name='video-lectures-list'),

    path('video-lectures/<int:pk>/', VideoLecturesDetail.as_view(),
         name='video-lectures-detail'),


]
