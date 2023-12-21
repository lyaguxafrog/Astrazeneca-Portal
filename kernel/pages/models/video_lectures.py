# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class VideoLectures(models.Model):
    video_article = models.CharField(max_length=255, verbose_name="Заголовок")
    conspect = models.TextField(verbose_name="Конспект видео")
    video = models.FileField(upload_to='video_lectures/')
    video_cover = models.ImageField(upload_to='video_covers/', verbose_name="Обложка видео")
    drug = models.OneToOneField("pages.Drug", on_delete=models.CASCADE)
    video_recomendations = models.ForeignKey('VideoLectures', on_delete=models.CASCADE, limit_choices_to={'video_article': models.F('video_recomendations__video_article')})
    access_number = models.CharField(max_length=255, verbose_name="Поле для добавления расшифровок и номеров одобрения")
    speciality = models.ForeignKey("pages.Specialty", on_delete=models.CASCADE)
    content_type = models.CharField(max_length=255, verbose_name="поле для выбора типа контента - видеолекции или видео кейс")
    saved_data = models.ForeignKey('pages.SavedByUser', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
