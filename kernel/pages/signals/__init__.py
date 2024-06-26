# -*- coding: utf-8 -*-

from .video_images import process_video_cover
from .story_images import process_avatar_story, process_cover_story
from .event_images import process_event_cover
from .articles_images import (process_articles_desktop_cover,
                              process_articles_mobile_cover,
                              process_article_main_cover_desktop,
                              process_article_main_cover_mobile)
from .drugs_images import process_drug_cover
from .search_signal import (create_last_adds_articles,
                            create_last_adds_event,
                            create_last_adds_video,
                            create_last_adds_drug,
                            delete_related_last_adds_article,
                            delete_related_last_adds_drug,
                            delete_related_last_adds_event,
                            delete_related_last_adds_video)
