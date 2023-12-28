# -*- coding: utf-8 -*-

from .story import StoryListAPIView, StoryDetailAPIView, SpecialityStoryListAPIView
from .article import ArticleDetailAPIView, ArticlesBySpecialtyAPIView
from .drugs import DrugDetailAPIView, DrugListAPIView
from .events import EventsAPIView
from .video import VideoLecturesDetail, VideoLecturesList
from .speciality import SpecialtyListAPIView

from .search import SearchResultsView
