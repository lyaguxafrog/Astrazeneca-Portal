# -*- coding: utf-8 -*-


from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from ckeditor.fields import RichTextField


class Articles(models.Model):
    ARTICLE_TYPE_CHOICES = [
        ('статья', 'Статья'),
        ('инновация', 'Инновация'),
    ]

    article_name = models.CharField(max_length=1024, verbose_name='Заголовок')
    cover = models.ImageField(upload_to='article_covers/',
                               blank=True, null=True, verbose_name="Обложка")
    first_abzac = RichTextField(verbose_name = "Первый абзац")
    short_description = RichTextField(verbose_name="Краткое описание")

    final_content = RichTextField(verbose_name = "Заключение")

    access_number = RichTextField(
        verbose_name="Поле для добавления расшифровок и номеров одобрения")
    speciality = models.ManyToManyField('pages.Specialty',
                            related_name='articles',
                            blank=True,
                            verbose_name="Специальности")

    drug = models.ManyToManyField('pages.Drug',
                                  blank=True,
                                  verbose_name='Препараты')

    article_type = models.CharField(max_length=255,
                            choices=ARTICLE_TYPE_CHOICES,
                            blank=True,
                            verbose_name='Тип статьи')

    information = RichTextField(verbose_name='текстовый блок для ввода инфы о статьи на разводящей станице статей')


    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.article_name


class ContentBlock(models.Model):
    ARTICLE_CONTENT_TYPE_CHOICES = [
        ('text', 'Текст'),
        ('quote', 'Цитата'),
        ('image', 'Изображение'),
        ('text_with_image', 'Текст с изображением'),
    ]

    article = models.ForeignKey('Articles', on_delete=models.CASCADE, related_name='content_blocks')
    content_type = models.CharField(max_length=16, choices=ARTICLE_CONTENT_TYPE_CHOICES, verbose_name='Тип контента')
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='content_block_images/', blank=True, null=True)
    order = models.PositiveIntegerField()
