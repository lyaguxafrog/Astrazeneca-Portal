# -*- coding: utf-8 -*-

from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

from ckeditor.fields import RichTextField
from polymorphic.models import PolymorphicModel


class Practicum(PolymorphicModel):
    title = models.CharField(verbose_name="Название практикума *",
                             max_length=90)
    image = models.ImageField(upload_to='practicum/',
                              verbose_name='Изображение *')

    desription = RichTextField(verbose_name='Описание *',
                                  max_length=200,
                                  help_text='Ограничение в 200 символов.')

    pacient_description = RichTextField(
                        verbose_name='Краткая информация о пациенте *',
                        help_text='Внутри практикума.',
                        default='''
                <p><span style="color:#00d1ff"><strong>Имя:</strong></span></p>
                <p><span style="color:#00d1ff"><strong>Возраст:</strong></span></p>
                <p><span style="color:#00d1ff"><strong>Образ жизни:</strong></span></p>
                <p><span style="color:#00d1ff"><strong>Семейный анамнез:</strong></span></p>
                <p><span style="color:#00d1ff"><strong>Перенесенные заболевания:</strong></span></p>
                <p><span style="color:#00d1ff"><strong>Оценка состояния:</strong></span></p>
                <p><span style="color:#00d1ff"><strong>Диагноз:</strong></span></p>
                            ''')

    priority = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(50)],
        verbose_name="Приоритет",
        default=50,
        help_text='Целое число от 1 до 50 включительно.'
    )

    speciality = models.ManyToManyField('pages.Specialty',
                                   related_name='practicum_speciality',
                                   blank=True, verbose_name='Специальность')

    # десктоп - 810px, 1620px, мобилка 400px, 800px
    image_desktop_810px = models.ImageField(upload_to='practicum/810px/',
                                            null=True, blank=True)
    image_desktop_1620px = models.ImageField(upload_to='practicum/1620px/',
                                             null=True, blank=True)
    image_mobile_400px = models.ImageField(upload_to='practicum/400px/',
                                           null=True, blank=True)
    image_mobile_800px = models.ImageField(upload_to='practicum/800px/',
                                           null=True, blank=True)

    class Meta:
        verbose_name='практикум'
        verbose_name_plural = 'практикумы'

    def __str__(self):
        return self.title
