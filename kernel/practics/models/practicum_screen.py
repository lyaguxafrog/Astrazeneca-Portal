# -*- coding: utf-8 -*-


from django.db import models
from ckeditor.fields import RichTextField


class Screens(models.Model):
    practicum = models.ForeignKey('Practicum', on_delete=models.CASCADE,
                                  related_name='screens')

    literature = RichTextField(null=True, blank=True)

    come_to_start = models.BooleanField(default=False)


# Блоки контента
class ScreenTextBlock(models.Model):
    screen = models.ForeignKey('Screens', on_delete=models.CASCADE,
                               related_name='screen_text_block')

    text = RichTextField()
    order = models.IntegerField(default=0)

class ScreenImageBlock(models.Model):
    screen = models.ForeignKey('Screens', on_delete=models.CASCADE)

    image = models.ImageField(upload_to='practicums/blocks/')
    order = models.IntegerField(default=0)

class ScreenPopupBlock(models.Model):
    screen = models.ForeignKey('Screens', on_delete=models.CASCADE,
                               related_name='screen_popup_block')

    menu_title = models.CharField()
    text = RichTextField()
    order = models.IntegerField(default=0)

class ScreenButton(models.Model):
    screen = models.ForeignKey('Screens', on_delete=models.CASCADE,
                               related_name='screen_button_block')
    button_title = models.CharField(null=True, blank=True)

    screen_number = models.IntegerField(default=None)
    screen_redirect = models.ForeignKey('Screens', on_delete=models.SET_NULL,
                null=True, blank=True, related_name='redirected_by_button')


    def save(self, *args, **kwargs):
        # Получаем экземпляр Practicum, к которому привязан Screens
        practicum = self.screen.practicum

        # Получаем экземпляр Screens по порядковому номеру
        try:
            screen_redirect = practicum.screens.all()[self.screen_number]
        except IndexError:
            screen_redirect = None

        # Устанавливаем связь
        self.screen_redirect = screen_redirect

        # Сохраняем изменения
        super(ScreenButton, self).save(*args, **kwargs)
