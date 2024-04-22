# -*- coding: utf-8 -*-

from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import FileExtensionValidator



class Drug(models.Model):
    name = models.CharField(max_length=90, verbose_name="Название препарата *",
                            help_text='Ограничение в 90 символов')
    brief_info = models.TextField(verbose_name="Краткое описание препарата *")

    image_desktop = models.ImageField(upload_to='drug_images/',
                        verbose_name="Изображение препарата для десктопа *")
    image_mobile = models.ImageField(upload_to='drug_images/',
                        verbose_name='Изображение препарата для мобильной *')

    application_practice_articles = models.ManyToManyField('pages.Articles',
                    blank=True, related_name='application_practice_articles',
                    verbose_name="Статьи в практике применения")

    application_practice_videos = models.ManyToManyField('pages.VideoLectures',
                    blank=True, related_name='application_practice_videos',
                    verbose_name="Видео в практике применения")

    approvals_and_decodings = RichTextField(verbose_name="Расшифровки и номера одобрения *")
    speciality = models.ManyToManyField("pages.Specialty", verbose_name='Специальность *')
    url_field = models.URLField(verbose_name="Ссылка на интрукцию в PDF", null=True, blank=True)
    file_field = models.FileField(verbose_name="Инструкция в формате PDF",
                        null=True, blank=True,
                        upload_to='pdf_files/',
                        validators= [
                        FileExtensionValidator(allowed_extensions=['pdf'])
                            ],
                        )

    priority = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(50)],
        verbose_name="Приоритет",
        default=50,
        help_text='Целое число от 1 до 50 включительно.'
    )


    image_desktop_1400px = models.ImageField(upload_to='drugs/1400px/', verbose_name="Изображение 1400px", null=True, blank=True)
    image_desktop_700px = models.ImageField(upload_to='drugs/700px/', verbose_name="Изображение 700px", null=True, blank=True)
    image_mobile_270px = models.ImageField(upload_to='drugs/270px/', verbose_name="Изображение 270px", null=True, blank=True)
    image_mobile_540px = models.ImageField(upload_to='drugs/540px/', verbose_name="Изображение 540px", null=True, blank=True)

    favorite_desktop_300px = models.ImageField(upload_to='drugs/ffavorites',
            null=True, blank=True)
    favorite_desktop_600px = models.ImageField(upload_to='drugs/ffavorites',
            null=True, blank=True)
    favorite_mobile_250px = models.ImageField(upload_to='drugs/ffavorites',
            null=True, blank=True)
    favorite_mobile_500px = models.ImageField(upload_to='drugs/ffavorites',
            null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'препарат'
        verbose_name_plural = 'препараты'

class DrugFAQ(models.Model):

    drug = models.ForeignKey('Drug', on_delete=models.CASCADE,
                             related_name="faq")
    title = models.CharField(verbose_name="Заголовок *")
    text = RichTextField(verbose_name="Текст *")
    approvals_and_decodings = RichTextField(verbose_name="Расшифровки и номера одобрения", null=True, blank=True)
    order = models.PositiveBigIntegerField(verbose_name='Порядковый номер *')

    class Meta:
        ordering = ['order']

class Icon(models.Model):
    IMAGE_TYPES = (
        ('image', 'Image'),
        ('svg', 'SVG'),
    )

    drug = models.ForeignKey('Drug', on_delete=models.CASCADE,
                    related_name='icons', verbose_name="Препарат")

    image_file = models.FileField(upload_to='icon_files/',
            verbose_name="Иконка *",
            help_text="Поддерживаются изображения и SVG", blank=True)

    def __str__(self):
        return str(self.image_file)
