# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Drug(models.Model):
    name = models.CharField(max_length=255,verbose_name="Название препарата")
    brief_info = models.TextField(verbose_name="Краткое описание препарата")
    image = models.ImageField(upload_to='drug_images/', verbose_name="Изображение препарата")
    icoins = models.ImageField(upload_to='drug_icons/', verbose_name="Иконки")
    instruction_points = models.TextField(verbose_name="Список названий пунктов инструкции")
    instruction_text = models.TextField(verbose_name="Текст пункта инструкции")
    application_practice = models.TextField(verbose_name="Практика применения")
    approvals_and_decodings = models.TextField(verbose_name="Расшифровки и номера одобрения")
    saved_data = models.ManyToManyField('pages.SavedByUser')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Препараты'
        verbose_name_plural = 'Препараты'
