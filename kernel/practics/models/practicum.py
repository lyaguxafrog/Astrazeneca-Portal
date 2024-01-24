# -*- coding: utf-8 -*-

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from sortedm2m.fields import SortedManyToManyField
from django.core.validators import MinValueValidator, MaxValueValidator


class Practicum(models.Model):
    title = models.CharField()
    image = models.ImageField(upload_to='practicum/')

    priority = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(50)],
        verbose_name="Приоритет",
        default=50,
        help_text='Целое число от 1 до 50 включительно.'
    )
