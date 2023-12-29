# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class Events(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название мероприятия")
    date = models.DateField(verbose_name="Дата мероприятия")
    cover = models.ImageField(upload_to='event_covers/')
    text = RichTextField(verbose_name="Описание мероприятия",
                         null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = "Мероприятия"


    def __str__(self):
        return (f"{self.name} | {self.date}")
