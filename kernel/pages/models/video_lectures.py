# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class VideoLectures(models.Model):
    VIDEO_TYPE_CHOICES = [
        ('видеолекция', 'Видеолекция'),
        ('клинические случаи', 'Клинические случаи'),
    ]

    video_article = models.CharField(max_length=90, verbose_name="Заголовок *",
                                     help_text='Ограничение в 90 символов')
    short_description = models.TextField(verbose_name='Краткое описание *')
    conspect = RichTextField(verbose_name="Конспект видео *")
    video = models.FileField(upload_to='video_lectures/', verbose_name='Видео *')
    video_cover_desktop = models.ImageField(upload_to='video_covers/', verbose_name="Обложка видео, десктоп *")
    video_cover_mobile = models.ImageField(upload_to='video_covers/', verbose_name="Обложка видео, мобильная *")
    drug = models.ManyToManyField("pages.Drug", blank=True, null=True, verbose_name='Препарат')
    video_recomendations = models.ManyToManyField('VideoLectures', null=True, blank=True,
                                            verbose_name='Видео-рекомендации')
    access_number = RichTextField(verbose_name="Поле для добавления расшифровок и номеров одобрения *")
    speciality = models.ManyToManyField("pages.Specialty", verbose_name='Специальность *')
    content_type = models.CharField(max_length=255, choices=VIDEO_TYPE_CHOICES, verbose_name="Поле для выбора типа контента *  ")

    video_cover_desktop_1400px = models.ImageField(upload_to='video_covers/1400px/', null=True, blank=True)
    video_cover_desktop_2800px = models.ImageField(upload_to='video_covers/2800px/', null=True, blank=True)
    recomendation_cover_desktop_500px = models.ImageField(upload_to='video_covers/recomendation/', null=True, blank=True)
    recomendation_cover_desktop_1000px = models.ImageField(upload_to='video_covers/recomendation/', null=True, blank=True)

    video_cover_mobile_390px = models.ImageField(upload_to='video_covers/390px/', null=True, blank=True)
    video_cover_mobile_780px = models.ImageField(upload_to='video_covers/780px/', null=True, blank=True)
    video_cover_mobile_420px = models.ImageField(upload_to='video_covers/420px/', null=True, blank=True)
    video_cover_mobile_840px = models.ImageField(upload_to='video_covers/840px/', null=True, blank=True)
    recomendation_cover_mobile_280px = models.ImageField(upload_to='video_covers/recomendation/', null=True, blank=True)
    recomendation_cover_mobile_560px = models.ImageField(upload_to='video_covers/recomendation/', null=True, blank=True)

    practic_desktop_400px = models.ImageField(null=True, blank=True,
        upload_to='video_covers/practic/')
    practic_desktop_800px = models.ImageField(null=True, blank=True,
        upload_to='video_covers/practic/')
    practic_mobile_280px = models.ImageField(null=True, blank=True,
        upload_to='video_covers/practic/')
    practic_mobile_560px = models.ImageField(null=True, blank=True,
        upload_to='video_covers/practic/')

    favorite_desktop_300px = models.ImageField(upload_to='video_covers/ffavorites',
            null=True, blank=True)
    favorite_desktop_600px = models.ImageField(upload_to='video_covers/ffavorites',
            null=True, blank=True)
    favorite_mobile_250px = models.ImageField(upload_to='video_covers/ffavorites',
            null=True, blank=True)
    favorite_mobile_500px = models.ImageField(upload_to='video_covers/ffavorites',
            null=True, blank=True)

    class Meta:
        verbose_name = 'видео'
        verbose_name_plural = 'видео'

    def __str__(self):
        return self.video_article
