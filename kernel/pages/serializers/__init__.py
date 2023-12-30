# -*- coding: utf-8 -*-

from .story import StorySerializer, StoryListSerializer
from .articles import (ArticlesSerializer, ContentBlockSerializer,
                       ArticlesBySpecialitySerializer)
from .drugs import DrugListSerializer, DrugSerializer
from .event import EventsSerializer
from .video import VideoLecturesListSerializer, VideoLecturesSerializer
from .speciality import SpecialtySerializer

from .search import SearchSerializer

from .main_page import MainPageApproveNumberSerializer
