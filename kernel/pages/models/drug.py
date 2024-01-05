# -*- coding: utf-8 -*-

from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from pathlib import Path
from io import BytesIO
from django.core.files import File
from PIL import Image


class Icon(models.Model):
    IMAGE_TYPES = (
        ('image', 'Image'),
        ('svg', 'SVG'),
    )

    drug = models.ForeignKey('Drug', on_delete=models.CASCADE,
                    related_name='icons_set', verbose_name="Препарат")

    image_file = models.FileField(upload_to='icon_files/',
            verbose_name="Иконка",
            help_text="Поддерживаются изображения и SVG", blank=True)

    def __str__(self):
        return str(self.image_file)

class DrugFAQ(models.Model):

    drug = models.ForeignKey('Drug', on_delete=models.CASCADE,
                             related_name="FAQ")
    title = models.CharField(verbose_name="Заголовок")
    text = RichTextField(verbose_name="Текст")
    order = models.PositiveBigIntegerField(verbose_name='Порядковый номер')


class Drug(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название препарата")
    brief_info = models.TextField(verbose_name="Краткое описание препарата")
    image = models.ImageField(upload_to='drug_images/', verbose_name="Изображение препарата")
    application_practice_articles = models.ManyToManyField('pages.Articles', blank=True, related_name='application_practice_articles', verbose_name="Статьи в практике применения")
    application_practice_videos = models.ManyToManyField('pages.VideoLectures', blank=True, related_name='application_practice_videos', verbose_name="Видео в практике применения")
    approvals_and_decodings = RichTextField(verbose_name="Расшифровки и номера одобрения")
    icons = models.ManyToManyField(Icon, blank=True, related_name='drugs', verbose_name="Иконки")
    faq = models.ManyToManyField(DrugFAQ, blank=True, related_name='drugs', verbose_name="FAQ")
    speciality = models.ManyToManyField("pages.Specialty", verbose_name='Специальность')
    url_field = models.URLField(verbose_name="Ссылка на интрукцию в PDF", null=True, blank=True)
    file_field = models.FileField(verbose_name="Инструкция в формате PDF", null=True, blank=True, upload_to='pdf_files/')

    image_1400px = models.ImageField(upload_to='drugs/1400px/', verbose_name="Изображение 1400px", null=True, blank=True)
    image_2800px = models.ImageField(upload_to='drugs/2800px/', verbose_name="Изображение 2800px", null=True, blank=True)
    image_390px = models.ImageField(upload_to='drugs/390px/', verbose_name="Изображение 390px", null=True, blank=True)
    image_780px = models.ImageField(upload_to='drugs/780px/', verbose_name="Изображение 780px", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Препарат'
        verbose_name_plural = 'Препараты'


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
@receiver(pre_save, sender=Drug)
def process_video_cover(sender, instance, **kwargs):
    if instance.image:
        file_path = instance.image.path

        # Проверяем, существует ли файл
        if Path(file_path).exists():
            # Отключаем сигналы для избежания рекурсии
            with DisableSignals(sender=Drug):
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
                instance.image_390px.save(f"{instance.image.name}_390px.jpg", File(image_stream_390px), save=False)

                image_stream_780px = BytesIO()
                image.resize((target_width_780, target_height_780)).save(image_stream_780px, format='JPEG')
                instance.image_780px.save(f"{instance.image.name}_780px.jpg", File(image_stream_780px), save=False)

                image_stream_1400px = BytesIO()
                image.resize((target_width_1400, target_height_1400)).save(image_stream_1400px, format='JPEG')
                instance.image_1400px.save(f"{instance.image.name}_1400px.jpg", File(image_stream_1400px), save=False)

                image_stream_2800px = BytesIO()
                image.resize((target_width_2800, target_height_2800)).save(image_stream_2800px, format='JPEG')
                instance.image_2800px.save(f"{instance.image.name}_2800px.jpg", File(image_stream_2800px), save=False)

                # Сохраняем изменения в модели вручную
                instance.save()
        else:
            print(f"Файл не найден: {file_path}")
