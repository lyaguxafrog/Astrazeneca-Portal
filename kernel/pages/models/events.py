# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from pathlib import Path
from io import BytesIO
from django.core.files import File
from PIL import Image



class Events(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название мероприятия")
    date = models.DateField(verbose_name="Дата мероприятия")
    cover = models.ImageField(upload_to='event_covers/', verbose_name='Обложка')
    text = RichTextField(verbose_name="Описание мероприятия",
                         null=True, blank=True)
    url = models.URLField(null=True, blank=True)


    image_1400px = models.ImageField(upload_to='events/1400px/', verbose_name="Изображение 1400px", null=True, blank=True)
    image_2800px = models.ImageField(upload_to='events/2800px/', verbose_name="Изображение 2800px", null=True, blank=True)
    image_390px = models.ImageField(upload_to='events/390px/', verbose_name="Изображение 390px", null=True, blank=True)
    image_780px = models.ImageField(upload_to='events/780px/', verbose_name="Изображение 780px", null=True, blank=True)



    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = "Мероприятия"


    def __str__(self):
        return (f"{self.name} | {self.date}")

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
@receiver(pre_save, sender=Events)
def process_video_cover(sender, instance, **kwargs):
    if instance.cover:
        file_path = instance.cover.path

        # Проверяем, существует ли файл
        if Path(file_path).exists():
            # Отключаем сигналы для избежания рекурсии
            with DisableSignals(sender=Events):
                image = Image.open(file_path)

                # Создаем байтовый поток и сохраняем изображения с разными размерами
                image_stream_1400px = BytesIO()
                image.resize((1400, 1400)).save(image_stream_1400px, format='JPEG')
                instance.image_1400px.save(f"{instance.cover.name}_1400px.jpg", File(image_stream_1400px), save=False)

                image_stream_2800px = BytesIO()
                image.resize((2800, 2800)).save(image_stream_2800px, format='JPEG')
                instance.image_2800px.save(f"{instance.cover.name}_2800px.jpg", File(image_stream_2800px), save=False)

                image_stream_390px = BytesIO()
                image.resize((390, 390)).save(image_stream_390px, format='JPEG')
                instance.image_390px.save(f"{instance.cover.name}_390px.jpg", File(image_stream_390px), save=False)

                image_stream_780px = BytesIO()
                image.resize((780, 780)).save(image_stream_780px, format='JPEG')
                instance.image_780px.save(f"{instance.cover.name}_780px.jpg", File(image_stream_780px), save=False)

                # Сохраняем изменения в модели вручную
                instance.save()
        else:
            print(f"Файл не найден: {file_path}")
