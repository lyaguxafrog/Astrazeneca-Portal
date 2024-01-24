# -*- coding: utf-8 -*-

from django.db import models
from ckeditor.fields import RichTextField


class Screens(models.Model):
    practicum = models.ForeignKey('Practicum', on_delete=models.CASCADE,
                                  related_name='screens')

    literature = RichTextField(null=True, blank=True)


# Блоки контента
class ScreenTextBlock(models.Model):
    screen = models.ForeignKey('Screens', on_delete=models.CASCADE,
                               related_name='screen_text_block')

    text = RichTextField()

class ScreenImageBlock(models.Model):
    screen = models.ForeignKey('Screens', on_delete=models.CASCADE)

    image = models.ImageField(upload_to='practicums/blocks/')

class ScreenPopupBlock(models.Model):
    screen = models.ForeignKey('Screens', on_delete=models.CASCADE,
                               related_name='screen_popup_block')

    menu_title = models.CharField()
    text = RichTextField()

class ScreenButton(models.Model):
    screen = models.ForeignKey('Screens', on_delete=models.CASCADE,
                               related_name='screen_button_block')

    button_title = models.CharField()
    screen = None # связь с экраном
    # ...
