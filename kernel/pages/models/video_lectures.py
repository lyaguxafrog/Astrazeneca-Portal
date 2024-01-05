# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from PIL import Image
from django.db.models.signals import pre_save
from django.dispatch import receiver
from pathlib import Path
from io import BytesIO
from django.core.files import File



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
        file_path = instance.video_cover.path

        # Проверяем, существует ли файл
        if Path(file_path).exists():
            # Отключаем сигналы для избежания рекурсии
            with DisableSignals(sender=VideoLectures):
                image = Image.open(file_path)

                # Определяем высоту и ширину оригинала
                original_width, original_height = image.size

                # Задаем высоту для измененных изображений
                target_height_390 = 390
                target_height_780 = 780
                target_height_1400 = 1400
                target_height_2800 = 2800

                # Рассчитываем новую ширину с сохранением пропорций
                target_width_390 = int(original_width / original_height * target_height_390)
                target_width_780 = int(original_width / original_height * target_height_780)
                target_width_1400 = int(original_width / original_height * target_height_1400)
                target_width_2800 = int(original_width / original_height * target_height_2800)

                # Масштабируем изображения с новыми размерами
                image_stream_390px = BytesIO()
                image.resize((target_width_390, target_height_390)).save(image_stream_390px, format='JPEG')
                instance.video_cover_390px.save(f"{instance.video_cover.name}_390px.jpg", File(image_stream_390px), save=False)

                image_stream_780px = BytesIO()
                image.resize((target_width_780, target_height_780)).save(image_stream_780px, format='JPEG')
                instance.video_cover_780px.save(f"{instance.video_cover.name}_780px.jpg", File(image_stream_780px), save=False)

                image_stream_1400px = BytesIO()
                image.resize((target_width_1400, target_height_1400)).save(image_stream_1400px, format='JPEG')
                instance.video_cover_1400px.save(f"{instance.video_cover.name}_1400px.jpg", File(image_stream_1400px), save=False)

                image_stream_2800px = BytesIO()
                image.resize((target_width_2800, target_height_2800)).save(image_stream_2800px, format='JPEG')
                instance.video_cover_2800px.save(f"{instance.video_cover.name}_2800px.jpg", File(image_stream_2800px), save=False)

                # Сохраняем изменения в модели вручную
                instance.save()
        else:
            print(f"Файл не найден: {file_path}")
