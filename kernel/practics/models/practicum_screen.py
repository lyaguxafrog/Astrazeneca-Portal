# -*- coding: utf-8 -*-


from django.db import models
from ckeditor.fields import RichTextField


class Screens(models.Model):
    practicum = models.ForeignKey('Practicum', on_delete=models.CASCADE,
                                  related_name='screens')

    literature = RichTextField(null=True, blank=True,
                               verbose_name='список литературы')

    come_to_start = models.BooleanField(default=False,
verbose_name='Добавить кнопку "В начало страницы"',
help_text='Отметьте, чтобы добавить кнопку "В начало страницы" на этом экране')

    class Meta:
        verbose_name = 'экран'
        verbose_name_plural = 'экраны'

# Блоки контента
class ScreenTextBlock(models.Model):
    screen = models.ForeignKey('Screens', on_delete=models.CASCADE,
                               related_name='screen_text_block')

    text = RichTextField(verbose_name='текст *')
    order = models.IntegerField(default=0, verbose_name='порядковый номер *')

    class Meta:
        verbose_name='блок текста'
        verbose_name_plural = 'блоки текста'

class ScreenImageBlock(models.Model):
    screen = models.ForeignKey('Screens', on_delete=models.CASCADE,
                               related_name='screen_image_block')

    image = models.ImageField(upload_to='practicums/blocks/',
                              verbose_name='изображение *')
    order = models.IntegerField(default=0)

    image_desktop_810px = models.ImageField(null=True, blank=True)
    image_desktop_1620px = models.ImageField(null=True, blank=True)
    image_mobile_400px = models.ImageField(null=True, blank=True)
    image_mobile_800px = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name='блок изображения'
        verbose_name_plural = 'блоки изображения'


class ScreenPopupBlock(models.Model):
    screen = models.ForeignKey('Screens', on_delete=models.CASCADE,
                               related_name='screen_popup_block')

    menu_title = models.CharField(verbose_name='Заголовок пункта *')
    text = RichTextField(verbose_name='Текст *')
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name='блок выпадающий список'
        verbose_name_plural = 'блоки выпадающий список'

class ScreenButton(models.Model):
    screen = models.ForeignKey('Screens', on_delete=models.CASCADE,
                               related_name='screen_button_block')

    button_title = models.CharField(null=True, blank=True,
                                    verbose_name='Заголовк кнопки *')

    screen_number = models.IntegerField(default=None,
verbose_name='Номер экрана',
help_text='Укажите номер экрана, на который будет перенаправлять эта кнопка')

    screen_redirect = models.ForeignKey('Screens', on_delete=models.SET_NULL,
                null=True, blank=True, related_name='redirected_by_button')

    class Meta:
        verbose_name='блок кнопки'
        verbose_name_plural = 'блоки кнопок'


    def save(self, *args, **kwargs):
        # Получаем экземпляр Practicum, к которому привязан Screens
        practicum = self.screen.practicum

        # Получаем экземпляр Screens по порядковому номеру (первый экран имеет номер 1)
        try:
            screen_redirect = practicum.screens.all()[self.screen_number - 1]
        except IndexError:
            screen_redirect = None

        # Устанавливаем связь
        self.screen_redirect = screen_redirect

        # Сохраняем изменения
        super(ScreenButton, self).save(*args, **kwargs)
