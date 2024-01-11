# -*- coding: utf-8 -*-

from .story import StoryListAPIView, StoryDetailAPIView, SpecialityStoryListAPIView
from .article import ArticleDetailAPIView, ArticlesBySpecialtyAPIView, ArticlesListAPIView
from .drugs import DrugDetailAPIView, DrugListAPIView
from .events import EventsAPIView
from .video import VideoLecturesDetail, VideoLecturesList, VideoLecturesListBySpecialty
from .speciality import SpecialtyListAPIView
from .main_page import MainPageApproveNumberAPIView
from .search import SearchAPIView, LastAddsListAPIView
