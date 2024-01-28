# -*- coding: utf-8 -*-

from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator


class Articles(models.Model):
    ARTICLE_TYPE_CHOICES = [
        ('article', 'Статья'),
        ('innovation', 'Инновация'),
    ]

    article_name = models.CharField(max_length=90, verbose_name='Заголовок *',
                                    help_text='Ограничение в 90 символов')
    main_cover_desktop = models.ImageField(upload_to='article_cover/',
                                   verbose_name='Главная картинка статьи(десктоп) *')
    main_cover_mobile = models.ImageField(upload_to='article_cover/',
                            verbose_name='Главная картинка статьи(мобильная) *')
    cover_desktop = models.ImageField(upload_to='article_covers/',
                               verbose_name="Обложка(десктоп) *")
    cover_mobile = models.ImageField(verbose_name='Обложка(мобильная) *',
                                upload_to='article_cover/')
    first_abzac = RichTextField(verbose_name = "Первый абзац *")
    final_content = RichTextField(verbose_name = "Заключение *")
    access_number = RichTextField(
        verbose_name="Поле для добавления расшифровок и номеров одобрения *")
    speciality = models.ManyToManyField('pages.Specialty',
                            related_name='articles',
                            blank=True,
                            verbose_name="Специальности")

    center_title = models.BooleanField(default=False, verbose_name='Заголовок по центру',
                                       help_text='Поставьте галочку, чтобы заголовок отображался по центру обложки')

    priority = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(50)],
        verbose_name="Приоритет",
        default=50,
        help_text='Целое число от 1 до 50 включительно.'
    )

    drug = models.ManyToManyField('pages.Drug',
                                  blank=True,
                                  verbose_name='Препараты')

    article_type = models.CharField(max_length=255,
                            choices=ARTICLE_TYPE_CHOICES,
                            verbose_name='Тип статьи *')

    information = RichTextField(verbose_name='текстовый блок для ввода инфы о статьи на разводящей станице статей *')

    cover_desktop_1400px = models.ImageField(upload_to='article_cover/1400px/',
                                             null=True, blank=True)
    cover_desktop_2800px = models.ImageField(upload_to='article_cover/2800px/',
                                             null=True, blank=True)
    cover_mobile_420px = models.ImageField(upload_to='article_cover/420px/',
                                           null=True, blank=True)
    cover_mobile_840px = models.ImageField(upload_to='article_cover/840px/',
                                           null=True, blank=True)

    main_cover_desktop_1600px = models.ImageField(
        upload_to='article_cover/main_cover/', null=True, blank=True)
    main_cover_desktop_3200px = models.ImageField(
        upload_to='article_cover/main_cover/', null=True, blank=True)
    main_cover_mobile_360px = models.ImageField(
        upload_to='article_cover/main_cover/', null=True, blank=True)
    main_cover_mobile_720px = models.ImageField(
        upload_to='article_cover/main_cover/', null=True, blank=True)

    practic_desktop_400px = models.ImageField(null=True, blank=True,
        upload_to='article_cover/practic/')
    practic_desktop_800px = models.ImageField(null=True, blank=True,
        upload_to='article_cover/practic/')
    practic_mobile_280px = models.ImageField(null=True, blank=True,
        upload_to='article_cover/practic/')
    practic_mobile_560px = models.ImageField(null=True, blank=True,
        upload_to='article_cover/practic/')

    favorite_desktop_300px = models.ImageField(upload_to='article_cover/ffavorites',
            null=True, blank=True)
    favorite_desktop_600px = models.ImageField(upload_to='article_cover/ffavorites',
            null=True, blank=True)
    favorite_mobile_250px = models.ImageField(upload_to='article_cover/ffavorites',
            null=True, blank=True)
    favorite_mobile_500px = models.ImageField(upload_to='article_cover/ffavorites',
            null=True, blank=True)


    class Meta:
        verbose_name = "статью"
        verbose_name_plural = "статьи"

    def __str__(self):
        return self.article_name


class ContentBlock(models.Model):
    ARTICLE_CONTENT_TYPE_CHOICES = [
        ('text', 'Текст'),
        ('quote', 'Цитата'),
        # ('image', 'Изображение'),
        # ('text_with_image', 'Текст с изображением'),
    ]

    article = models.ForeignKey('Articles', on_delete=models.CASCADE, related_name='content_blocks')
    content_type = models.CharField(max_length=16, choices=ARTICLE_CONTENT_TYPE_CHOICES, verbose_name='Тип контента *')
    text = models.TextField(blank=True, null=True, verbose_name='Текст')
    image = models.ImageField(upload_to='content_block_images/',
                              blank=True, null=True, verbose_name='Изображение')
    order = models.PositiveIntegerField(verbose_name='Поорядковый номер *')

    class Meta:
        verbose_name = 'блоки контента'
        verbose_name_plural = 'блоки контента'
