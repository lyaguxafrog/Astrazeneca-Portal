# -*- coding: utf-8 -*-

from haystack import indexes
from pages.models import Articles, Drug, VideoLectures


class ArticlesIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Articles
