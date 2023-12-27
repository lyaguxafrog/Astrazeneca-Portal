# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from jsonfield import JSONField
from ckeditor.fields import RichTextField


class Drug(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название препарата")
    brief_info = models.TextField(verbose_name="Краткое описание препарата")
    image = models.ImageField(upload_to='drug_images/', verbose_name="Изображение препарата")
    icoins = JSONField(verbose_name="Иконки", blank=True, null=True)
    instruction_points = models.TextField(verbose_name="Список названий пунктов инструкции")
    instruction_text = RichTextField(verbose_name="Текст инструкции")
    application_practice = RichTextField(verbose_name="Практика применения")
    approvals_and_decodings = RichTextField(verbose_name="Расшифровки и номера одобрения")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Препараты'
        verbose_name_plural = 'Препараты'
