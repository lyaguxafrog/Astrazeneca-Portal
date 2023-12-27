# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Story(models.Model):
    avatar = models.ImageField(upload_to='story_avatars/')
    title = models.CharField(max_length=255)
    content = models.TextField()
    video = models.FileField(upload_to='story_videos/',
                             null=True, blank=True)
    cover_image = models.ImageField(upload_to='story_covers/',
                                    null=True, blank=True)
    link_to_page = models.URLField()
    specialties = models.ManyToManyField('pages.Specialty')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Истории'
        verbose_name_plural = 'Истории'
