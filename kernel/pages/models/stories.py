# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Story(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='story_avatars/')
    title = models.CharField(max_length=255)
    content = models.TextField()
    video = models.FileField(upload_to='story_videos/', null=True, blank=True, verbose_name='Видео')
    cover_image = models.ImageField(upload_to='story_covers/', null=True, blank=True, verbose_name='Обложка')
    link_to_page = models.URLField(null=True, blank=True, verbose_name='Ссылка на страницу')
    specialties = models.ManyToManyField('pages.Specialty', verbose_name='Специальности')
    is_active = models.BooleanField(default=True, verbose_name='Статус отображения')

    def __str__(self):
        return self.title
