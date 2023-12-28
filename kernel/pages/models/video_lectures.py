# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class VideoLectures(models.Model):
    VIDEO_TYPE_CHOICES = [
        ('видеолекция', 'Видеолекция'),
        ('кейс', 'Кейс'),
    ]

    video_article = models.CharField(max_length=255, verbose_name="Заголовок")
    short_description = models.TextField(verbose_name='Краткое описание')
    conspect = RichTextField(verbose_name="Конспект видео")
    video = models.FileField(upload_to='video_lectures/', verbose_name='Видео')
    video_cover = models.ImageField(upload_to='video_covers/', verbose_name="Обложка видео")
    drug = models.OneToOneField("pages.Drug", on_delete=models.CASCADE, blank=True, null=True, verbose_name='Препарат')
    video_recomendations = models.ManyToManyField('VideoLectures', null=True, blank=True)
    access_number = RichTextField(verbose_name="Поле для добавления расшифровок и номеров одобрения")
    speciality = models.ManyToManyField("pages.Specialty", verbose_name='Специальность')
    content_type = models.CharField(max_length=255, choices=VIDEO_TYPE_CHOICES, verbose_name="Поле для выбора типа контента")

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return self.video_article
