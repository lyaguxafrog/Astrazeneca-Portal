# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _


class Story(models.Model):
    COLOR_CHOISE = [
    ('#00D1FF', 'Синий 🟦'),
    ('#E130FF', 'Фиолетовый 🟪' ),
    ('#fff', 'Белый ⬜')
]

    avatar = models.ImageField(upload_to='story_avatars/', verbose_name='Аватар *')
    title = models.CharField(max_length=255, verbose_name='Имя *')
    content = models.TextField(verbose_name='Контент *')
    video = models.FileField(upload_to='story_videos/', verbose_name='Видео *')
    cover_image = models.ImageField(upload_to='story_covers/', verbose_name='Обложка *')
    link_to_page = models.URLField(null=True, blank=True, verbose_name='URL на страницу')
    specialties = models.ManyToManyField('pages.Specialty',
                                         blank=True, null=True, verbose_name='Специальность')
    is_active = models.BooleanField(default=True, verbose_name='Активность истории')

    color = models.CharField(max_length=255, choices=COLOR_CHOISE,
                             verbose_name="Цвет *")


    avatar_desktop_120px = models.ImageField(null=True, blank=True)
    avatar_desktop_280px = models.ImageField(null=True, blank=True)
    avatar_mobile_70px = models.ImageField(null=True, blank=True)
    avatar_mobile_140px = models.ImageField(null=True, blank=True)

    cover_450px = models.ImageField(null=True, blank=True)
    cover_900px = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Истории'
        verbose_name_plural = 'Истории'
