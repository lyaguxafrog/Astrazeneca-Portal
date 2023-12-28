# -*- coding: utf-8 -*-


from haystack import indexes
from pages.models import Articles, Drug, VideoLectures
from django.utils.translation import gettext_lazy as _


class ArticlesIndex(indexes.SearchIndex, indexes.Indexable):
    article = indexes.CharField(document=True, use_template=True)
    final_content = indexes.CharField(model_attr='final_content')
    article_name = indexes.CharField(model_attr='article_name')

    def get_model(self):
        return Articles

class DrugIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # Добавьте другие поля, если необходимо

    def get_model(self):
        return Drug

class VideoLecturesIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    video_article = indexes.CharField(model_attr='video_article')
    conspect = indexes.CharField(model_attr='conspect')

    def get_model(self):
        return VideoLectures
