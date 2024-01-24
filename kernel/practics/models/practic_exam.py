# -*- coding: utf-8 -*-

from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator

class PrTest(models.Model):
    title = models.CharField()

    question = RichTextField()
    image = models.ImageField(upload_to='practics/test/')

    priority = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(50)],
        verbose_name="Приоритет",
        default=50,
        help_text='Целое число от 1 до 50 включительно.'
    )
