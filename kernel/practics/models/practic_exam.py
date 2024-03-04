# -*- coding: utf-8 -*-

from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator

class PrTest(models.Model):
    title = models.CharField(verbose_name="Название теста *",
                             max_length=60, help_text='Ограничение в 60 символов.')

    question = RichTextField(verbose_name='Описание задания *')
    image = models.ImageField(upload_to='practics/test/',
                              verbose_name='Изображение *')

    speciality = models.ManyToManyField('pages.Specialty',
                                   related_name='prtest_speciality',
                                   blank=True, verbose_name='Специальность')

    priority = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(50)],
        verbose_name="Приоритет",
        default=50,
        help_text='Целое число от 1 до 50 включительно.'
    )

    approvals_and_decodings = RichTextField(null=True, blank=True,
                                verbose_name='Номер одобрения и расшифровка')

    next_test = models.OneToOneField('PrTest', null=True, blank=True,
                                       verbose_name='Следующий тест',
                                       on_delete=models.SET_NULL)

    # десктоп - 810px, 1620px, мобилка 400px, 800px
    image_desktop_810px = models.ImageField(upload_to='practics/test/810px',
                                            null=True, blank=True)
    image_desktop_1620px = models.ImageField(upload_to='practics/test/1620px',
                                             null=True, blank=True)
    image_mobile_400px = models.ImageField(upload_to='practics/test/400px',
                                           null=True, blank=True)
    image_mobile_800px = models.ImageField(upload_to='practics/test/800px',
                                           null=True, blank=True)
    class Meta:
        verbose_name = "тест"
        verbose_name_plural = "тесты"

    def __str__(self):
        return self.title

class AnswerButtons(models.Model):
    prtest = models.ForeignKey('PrTest', on_delete=models.CASCADE,
                                related_name='buttons')

    title = models.CharField(verbose_name='Заголовок кнопки *')
    text = RichTextField(verbose_name='Текст *')

    class Meta:
        verbose_name = 'вариант ответа'
        verbose_name_plural = 'варианты ответа'
