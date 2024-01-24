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

    # десктоп - 810px, 1620px, мобилка 400px, 800px
    image_desktop_810px = models.ImageField(upload_to='practics/test/810px',
                                            null=True, blank=True)
    image_desktop_1620px = models.ImageField(upload_to='practics/test/1620px',
                                             null=True, blank=True)
    image_mobile_400px = models.ImageField(upload_to='practics/test/400px',
                                           null=True, blank=True)
    image_mobile_800px = models.ImageField(upload_to='practics/test/800px',
                                           null=True, blank=True)


class AnswerButtons(models.Model):
    prtest = models.ForeignKey('PrTest', on_delete=models.CASCADE)

    title = models.CharField()
    teext = RichTextField()
