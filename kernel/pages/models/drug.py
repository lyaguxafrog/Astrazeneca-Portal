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

    image_desktop = models.ImageField(upload_to='drug_images/', verbose_name="Изображение препарата для десктопа")
    image_mobile = models.ImageField(upload_to='drug_images/', verbose_name='Изображение препарата для мобильной')

    application_practice_articles = models.ManyToManyField('pages.Articles', blank=True, related_name='application_practice_articles', verbose_name="Статьи в практике применения")
    application_practice_videos = models.ManyToManyField('pages.VideoLectures', blank=True, related_name='application_practice_videos', verbose_name="Видео в практике применения")
    approvals_and_decodings = RichTextField(verbose_name="Расшифровки и номера одобрения")
    icons = models.ManyToManyField(Icon, blank=True, related_name='drugs', verbose_name="Иконки")
    faq = models.ManyToManyField(DrugFAQ, blank=True, related_name='drugs', verbose_name="FAQ")
    speciality = models.ManyToManyField("pages.Specialty", verbose_name='Специальность')
    url_field = models.URLField(verbose_name="Ссылка на интрукцию в PDF", null=True, blank=True)
    file_field = models.FileField(verbose_name="Инструкция в формате PDF", null=True, blank=True, upload_to='pdf_files/')


    image_desktop_1400px = models.ImageField(upload_to='drugs/1400px/', verbose_name="Изображение 1400px", null=True, blank=True)
    image_desktop_700px = models.ImageField(upload_to='drugs/700px/', verbose_name="Изображение 700px", null=True, blank=True)
    image_mobile_270px = models.ImageField(upload_to='drugs/270px/', verbose_name="Изображение 270px", null=True, blank=True)
    image_mobile_540px = models.ImageField(upload_to='drugs/540px/', verbose_name="Изображение 540px", null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Препарат'
        verbose_name_plural = 'Препараты'

# блять почему я этим на бекенде занимаюсь
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
def process_drug_cover(sender, instance, **kwargs):
    if instance.image_desktop:
        file_path = instance.image_desktop.path

        # Проверяем, существует ли файл
        if Path(file_path).exists():
            # Отключаем сигналы для избежания рекурсии
            with DisableSignals(sender=Drug):
                image = Image.open(file_path)

                # Определяем высоту и ширину оригинала
                original_width, original_height = image.size

                # Задаем новую ширину для измененных изображений
                target_width_700 = 700
                target_width_1400 = 1400

                # Рассчитываем новую высоту с сохранением пропорций
                target_height_700 = int(original_height / original_width * target_width_700)
                target_height_1400 = int(original_height / original_width * target_width_1400)

                # Масштабируем изображения с новыми размерами
                image_stream_700px = BytesIO()
                image.resize((target_width_700, target_height_700)).save(image_stream_700px, format='PNG')
                instance.image_desktop_700px.save(f"{instance.image_desktop.name}_700px.png", File(image_stream_700px), save=False)

                image_stream_1400px = BytesIO()
                image.resize((target_width_1400, target_height_1400)).save(image_stream_1400px, format='PNG')
                instance.image_desktop_1400px.save(f"{instance.image_desktop.name}_1400px.png", File(image_stream_1400px), save=False)

                # Сохраняем изменения в модели вручную
                instance.save()
        else:
            print(f"Файл не найден: {file_path}")


        if instance.image_mobile:
            file_path = instance.image_mobile.path

            # Проверяем, существует ли файл
            if Path(file_path).exists():
                # Отключаем сигналы для избежания рекурсии
                with DisableSignals(sender=Drug):
                    image = Image.open(file_path)

                    # Определяем высоту и ширину оригинала
                    original_width, original_height = image.size

                    # Задаем новую ширину для измененных изображений
                    target_width_270 = 270
                    target_width_540 = 540

                    # Рассчитываем новую высоту с сохранением пропорций
                    target_height_270 = int(original_height / original_width * target_width_270)
                    target_height_540 = int(original_height / original_width * target_width_540)

                    # Масштабируем изображения с новыми размерами
                    image_stream_270px = BytesIO()
                    image.resize((target_width_270, target_height_270)).save(image_stream_270px, format='PNG')
                    instance.image_mobile_270px.save(f"{instance.image_mobile.name}_270px.png", File(image_stream_270px), save=False)

                    image_stream_540px = BytesIO()
                    image.resize((target_width_540, target_height_540)).save(image_stream_540px, format='PNG')
                    instance.image_mobile_540px.save(f"{instance.image_mobile.name}_540px.png", File(image_stream_540px), save=False)

                    # Сохраняем изменения в модели вручную
                    instance.save()
