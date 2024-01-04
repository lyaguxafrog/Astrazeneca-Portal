# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from PIL import Image
from django.db.models.signals import pre_save
from django.dispatch import Signal, receiver
from pathlib import Path
from io import BytesIO


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
    drug = models.ManyToManyField("pages.Drug", blank=True, null=True, verbose_name='Препарат')
    video_recomendations = models.ManyToManyField('VideoLectures', null=True, blank=True)
    access_number = RichTextField(verbose_name="Поле для добавления расшифровок и номеров одобрения")
    speciality = models.ManyToManyField("pages.Specialty", verbose_name='Специальность')
    content_type = models.CharField(max_length=255, choices=VIDEO_TYPE_CHOICES, verbose_name="Поле для выбора типа контента")

    video_cover_1400px = models.ImageField(upload_to='video_covers/1400px/', verbose_name="Обложка видео 1400px", null=True, blank=True)
    video_cover_2800px = models.ImageField(upload_to='video_covers/2800px/', verbose_name="Обложка видео 2800px", null=True, blank=True)
    video_cover_390px = models.ImageField(upload_to='video_covers/390px/', verbose_name="Обложка видео 390px", null=True, blank=True)
    video_cover_780px = models.ImageField(upload_to='video_covers/780px/', verbose_name="Обложка видео 780px", null=True, blank=True)

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return self.video_article


class DisableSignals:
    def __init__(self, sender):
        self.sender = sender
        self._receivers = None

    def __enter__(self):
        self._receivers = pre_save.receivers
        pre_save.receivers = []

    def __exit__(self, exc_type, exc_value, traceback):
        pre_save.receivers = self._receivers

# Обработчик сигнала pre_save
@receiver(pre_save, sender=VideoLectures)
def process_video_cover(sender, instance, **kwargs):
    if instance.video_cover:
        file_path = Path(instance.video_cover.path)

        # Check if the file exists
        if file_path.exists():
            # Disable signals to avoid recursion
            with DisableSignals(sender=VideoLectures):
                image = Image.open(file_path)

                # Create and save images with different sizes
                instance.video_cover_1400px.save(f"{instance.video_cover.name}_1400px.jpg", BytesIO(image.resize((1400, 1400)).tobytes()), save=False)
                instance.video_cover_2800px.save(f"{instance.video_cover.name}_2800px.jpg", BytesIO(image.resize((2800, 2800)).tobytes()), save=False)
                instance.video_cover_390px.save(f"{instance.video_cover.name}_390px.jpg", BytesIO(image.resize((390, 390)).tobytes()), save=False)
                instance.video_cover_780px.save(f"{instance.video_cover.name}_780px.jpg", BytesIO(image.resize((780, 780)).tobytes()), save=False)

                # Manually save changes to the model instance
                instance.save()
        else:
            print(f"File not found: {file_path}")
