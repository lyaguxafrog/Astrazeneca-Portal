# -*- coding: utf-8 -*-


from django.db import models


class Specialty(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название специальности *')
    image = models.ImageField(upload_to='specialty_images/', verbose_name='Изображение *')
    pro = models.CharField(verbose_name="PRO-", null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'специальность'
        verbose_name_plural = 'специальности'
