# -*- coding: utf-8 -*-

from django.db import models


class Articles(models.Model):
    article_name = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='article_covers/')
    article_text = models.TextField()
    quote = models.TextField()
    quote_image = models.ImageField(upload_to='quote_images/')

    drug_url = models.URLField()
    drug = models.ManyToManyField('pages.Drug', related_name='articles')
    final_content = models.CharField(max_length=255)

    access_number = models.CharField(max_length=255, verbose_name="Поле для добавления расшифровок и номеров одобрения")
    speciality = models.ManyToManyField('pages.Specialty', related_name='articles')
    article_type = models.CharField(max_length=255)
    saved_data = models.ForeignKey("pages.SavedByUser", on_delete=models.CASCADE, null=True)


    class Meta:
        verbose_name_plural = "Статьи"
