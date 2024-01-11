# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField



class Events(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название мероприятия *")
    date = models.DateField(verbose_name="Дата окончания мероприятия *")
    cover = models.ImageField(upload_to='event_covers/', verbose_name='Обложка *')
    text = RichTextField(verbose_name="Описание мероприятия(для поиска)")
    url = models.URLField(verbose_name='URL мероприятия *')


    image_desktop_570px = models.ImageField(upload_to='events/570px/', null=True, blank=True)
    image_desktop_1140px = models.ImageField(upload_to='events/1140px/', null=True, blank=True)
    image_mobile_540px = models.ImageField(upload_to='events/270px/', null=True, blank=True)
    image_mobile_270px = models.ImageField(upload_to='events/540px/', null=True, blank=True)



    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = "Мероприятия"


    def __str__(self):
        return (f"{self.name} | {self.date}")
