# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor.fields import RichTextField


class Practicum(models.Model):
    title = models.CharField()
    image = models.ImageField(upload_to='practicum/', null=True, blank=True)

    priority = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(50)],
        verbose_name="Приоритет",
        default=50,
        help_text='Целое число от 1 до 50 включительно.'
    )

    literature = RichTextField(null=True, blank=True)

    # десктоп - 810px, 1620px, мобилка 400px, 800px
    image_desktop_810px = models.ImageField(upload_to='practicum/810px/',
                                            null=True, blank=True)
    image_desktop_1620px = models.ImageField(upload_to='practicum/1620px/',
                                             null=True, blank=True)
    image_mobile_400px = models.ImageField(upload_to='practicum/400px/',
                                           null=True, blank=True)
    image_mobile_800px = models.ImageField(upload_to='practicum/800px/',
                                           null=True, blank=True)

    def __str__(self):
        return self.title
