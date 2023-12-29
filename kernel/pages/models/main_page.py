# -*- coding: utf-8 -*-


from django.db import models
from ckeditor.fields import RichTextField

class MainPageApproveNumber(models.Model):
    number = RichTextField(verbose_name="Номер одобрения")

    def __str__(self):
        return "Номер одобрения на главной странице"

    def save(self, *args, **kwargs):
        existing_instance = MainPageApproveNumber.objects.first()

        if existing_instance:
            existing_instance.number = self.number
            existing_instance.save()
        else:
            super(MainPageApproveNumber, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'
