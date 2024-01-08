# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField



class Events(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название мероприятия")
    date = models.DateField(verbose_name="Дата мероприятия")
    cover = models.ImageField(upload_to='event_covers/', verbose_name='Обложка')
    text = RichTextField(verbose_name="Описание мероприятия(для поиска)",
                         null=True, blank=True)
    url = models.URLField(null=True, blank=True)


    image_1400px = models.ImageField(upload_to='events/1400px/', verbose_name="Изображение 1400px", null=True, blank=True)
    image_2800px = models.ImageField(upload_to='events/2800px/', verbose_name="Изображение 2800px", null=True, blank=True)
    image_390px = models.ImageField(upload_to='events/390px/', verbose_name="Изображение 390px", null=True, blank=True)
    image_780px = models.ImageField(upload_to='events/780px/', verbose_name="Изображение 780px", null=True, blank=True)



    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = "Мероприятия"


    def __str__(self):
        return (f"{self.name} | {self.date}")
