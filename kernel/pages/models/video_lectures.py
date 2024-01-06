# -*- coding: utf-8 -*-

from distutils.command import upload
from tkinter.tix import Tree
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
    video_cover_desktop = models.ImageField(upload_to='video_covers/', verbose_name="Обложка видео, десктоп", blank=True, null=True)
    video_cover_mobile = models.ImageField(upload_to='video_covers/', verbose_name="Обложка видео, мобильная", blank=True, null=True)
    drug = models.ManyToManyField("pages.Drug", blank=True, null=True, verbose_name='Препарат')
    video_recomendations = models.ManyToManyField('VideoLectures', null=True, blank=True)
    access_number = RichTextField(verbose_name="Поле для добавления расшифровок и номеров одобрения")
    speciality = models.ManyToManyField("pages.Specialty", verbose_name='Специальность')
    content_type = models.CharField(max_length=255, choices=VIDEO_TYPE_CHOICES, verbose_name="Поле для выбора типа контента")

    video_cover_desktop_1400px = models.ImageField(upload_to='video_covers/1400px/', null=True, blank=True)
    video_cover_desktop_2800px = models.ImageField(upload_to='video_covers/2800px/', null=True, blank=True)
    recomendation_cover_desktop_430px = models.ImageField(upload_to='video_covers/recomendation/', null=True, blank=True)
    recomendation_cover_desktop_860px = models.ImageField(upload_to='video_covers/recomendation/', null=True, blank=True)

    video_cover_mobile_420px = models.ImageField(upload_to='video_covers/420px/', null=True, blank=True)
    video_cover_mobile_840px = models.ImageField(upload_to='video_covers/840px/', null=True, blank=True)
    recomendation_cover_mobile_270px = models.ImageField(upload_to='video_covers/recomendation/', null=True, blank=True)
    recomendation_cover_mobile_540px = models.ImageField(upload_to='video_covers/recomendation/', null=True, blank=True)


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
    if instance.video_cover_desktop:
        file_path = instance.video_cover_desktop.path

        # Проверяем, существует ли файл
        if Path(file_path).exists():
            # Отключаем сигналы для избежания рекурсии
            with DisableSignals(sender=VideoLectures):
                image = Image.open(file_path)

                # Определяем высоту и ширину оригинала
                original_width, original_height = image.size

                # Задаем новую ширину для измененных изображений
                target_width_2800 = 2800
                target_width_1400 = 1400
                target_width_430 = 430
                target_width_860 = 860

                # Рассчитываем новую высоту с сохранением пропорций
                target_height_2800 = int(original_height / original_width * target_width_2800)
                target_height_1400 = int(original_height / original_width * target_width_1400)
                target_height_430 = int(original_height / original_width * target_width_430)
                target_height_860 = int(original_height / original_width * target_width_860)

                # Масштабируем изображения с новыми размерами
                image_stream_2800px = BytesIO()
                image.resize((target_width_2800, target_height_2800)).save(image_stream_2800px, format='PNG')
                instance.video_cover_desktop_2800px.save(f"{instance.video_cover_desktop.name}_2800px.png", File(image_stream_2800px), save=False)

                image_stream_1400px = BytesIO()
                image.resize((target_width_1400, target_height_1400)).save(image_stream_1400px, format='PNG')
                instance.video_cover_desktop_1400px.save(f"{instance.video_cover_desktop.name}_1400px.png", File(image_stream_1400px), save=False)

                image_stream_430px = BytesIO()
                image.resize((target_width_430, target_height_430)).save(image_stream_430px, format='PNG')
                instance.recomendation_cover_desktop_430px.save(f"{instance.video_cover_desktop.name}_430px.png", File(image_stream_430px), save=False)

                image_stream_860px = BytesIO()
                image.resize((target_width_860, target_height_860)).save(image_stream_860px, format='PNG')
                instance.recomendation_cover_desktop_860px.save(f"{instance.video_cover_desktop.name}_860px.png", File(image_stream_860px), save=False)

                # Сохраняем изменения в модели вручную
                instance.save()

        else:
            print(f"Файл не найден: {file_path}")


    if instance.video_cover_mobile:
        file_path = instance.video_cover_mobile.path

        # Проверяем, существует ли файл
        if Path(file_path).exists():
            # Отключаем сигналы для избежания рекурсии
            with DisableSignals(sender=VideoLectures):
                image = Image.open(file_path)

                # Определяем высоту и ширину оригинала
                original_width, original_height = image.size

                # Задаем новую ширину для измененных изображений
                target_width_420 = 420
                target_width_840 = 840
                target_width_270 = 270
                target_width_540 = 540

                # Рассчитываем новую высоту с сохранением пропорций
                target_height_420= int(original_height / original_width * target_width_420)
                target_height_840 = int(original_height / original_width * target_width_840)
                target_height_270 = int(original_height / original_width * target_width_270)
                target_height_540 = int(original_height / original_width * target_width_540)

                # Масштабируем изображения с новыми размерами
                image_stream_420px = BytesIO()
                image.resize((target_width_420, target_height_420)).save(image_stream_420px, format='PNG')
                instance.video_cover_mobile_420px.save(f"{instance.video_cover_mobile.name}_420px.png", File(image_stream_420px), save=False)

                image_stream_840px = BytesIO()
                image.resize((target_width_840, target_height_840)).save(image_stream_840px, format='PNG')
                instance.video_cover_mobile_840px.save(f"{instance.video_cover_mobile.name}_840px.png", File(image_stream_840px), save=False)

                image_stream_270x = BytesIO()
                image.resize((target_width_270, target_height_270)).save(image_stream_270x, format='PNG')
                instance.recomendation_cover_mobile_270px.save(f"{instance.video_cover_mobile.name}_270px.png", File(image_stream_270x), save=False)

                image_stream_540px = BytesIO()
                image.resize((target_width_860, target_height_860)).save(image_stream_860px, format='PNG')
                instance.recomendation_cover_desktop_860px.save(f"{instance.video_cover_mobile.name}_860px.png", File(image_stream_860px), save=False)

                # Сохраняем изменения в модели вручную
                instance.save()

        else:
            print(f"Файл не найден: {file_path}")
