# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Events(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название мероприятия")
    date = models.CharField(max_length=255, verbose_name="Дата мероприятия")
    cover = models.ImageField(upload_to='event_covers/')
    url = models.URLField()

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = "Мероприятия"
