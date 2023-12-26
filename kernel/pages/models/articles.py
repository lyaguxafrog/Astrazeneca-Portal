# -*- coding: utf-8 -*-

from django.db import models

class Articles(models.Model):
    ARTICLE_TYPE_CHOICES = [
        ('статья', 'Статья'),
        ('инновация', 'Инновация'),
    ]

    article_name = models.CharField(max_length=1024, blank=True, verbose_name='Заголовок')
    cover = models.ImageField(upload_to='article_covers/', blank=True, null=True)
    article_text = models.TextField(blank=True)
    quote = models.TextField(blank=True)
    quote_image = models.ImageField(upload_to='quote_images/', blank=True, null=True)

    drug_url = models.URLField(null=True, blank=True)
    drug = models.ManyToManyField('pages.Drug', related_name='articles', blank=True)
    final_content = models.CharField(max_length=255, blank=True)

    access_number = models.CharField(max_length=255, verbose_name="Поле для добавления расшифровок и номеров одобрения", blank=True)
    speciality = models.ManyToManyField('pages.Specialty', related_name='articles', blank=True)
    article_type = models.CharField(max_length=255, choices=ARTICLE_TYPE_CHOICES, blank=True)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
