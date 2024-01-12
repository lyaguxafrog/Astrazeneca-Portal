# -*- coding: utf-8 -*-

from django.db import models
from ckeditor.fields import RichTextField

class SingletonModelManager(models.Manager):
    def get_or_create_singleton(self):
        obj, created = self.get_or_create(pk=1)
        return obj

class SingletonModel(models.Model):
    class Meta:
        abstract = True

    objects = SingletonModelManager()

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

class MainPageApproveNumber(SingletonModel):
    number = RichTextField(verbose_name="Номер одобрения *", help_text='Существует в едином экземпляре.')

    def __str__(self):
        return "Номер одобрения на главной странице"

    class Meta:
        verbose_name = 'футер'
        verbose_name_plural = 'футер'
