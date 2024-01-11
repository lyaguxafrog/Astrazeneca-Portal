# -*- coding: utf-8 -*-


from django.urls import path
from rest_framework import views
from .views import (StoryListAPIView, StoryDetailAPIView,
               ArticleDetailAPIView, DrugListAPIView,
               SpecialityStoryListAPIView,
               DrugDetailAPIView, EventsAPIView, ArticlesBySpecialtyAPIView,
               VideoLecturesList, VideoLecturesDetail, SpecialtyListAPIView,
               MainPageApproveNumberAPIView, SearchAPIView,
               VideoLecturesListBySpecialty, LastAddsListAPIView)

urlpatterns = [

    path('specialty', SpecialtyListAPIView.as_view(),
         name='specialty'),

     path('articles/specialty/<int:specialty_id>/',
          ArticlesBySpecialtyAPIView.as_view(), name='articles_by_specialty'),

     path('stories/', StoryListAPIView.as_view(), name='story-list'),
     path('stories/<int:id>/', SpecialityStoryListAPIView.as_view(), name='specialty-story-list'),

     path('main_page', MainPageApproveNumberAPIView.as_view(), name='main-page'),

     path('articles/<int:id>', ArticleDetailAPIView.as_view(),
         name='article'),

    path('search/<str:query>/', SearchAPIView.as_view(), name='search_api'),
    path('search/page', LastAddsListAPIView.as_view(),
         name='lastadds-list'),

    path('drugs/', DrugListAPIView.as_view(), name='drugs-list'),

    path('drugs/<int:pk>/', DrugDetailAPIView.as_view(), name='drugs-detail'),

    path('events/', EventsAPIView.as_view(), name='events-list'),

    path('video-lectures/', VideoLecturesList.as_view(),
         name='video-lectures-list'),

    path('video-lectures/speciality/<int:id>', VideoLecturesListBySpecialty.as_view(),
         name='video-lectures-list-by-specialty'),

    path('video-lectures/<int:pk>/', VideoLecturesDetail.as_view(),
         name='video-lectures-detail'),


]
