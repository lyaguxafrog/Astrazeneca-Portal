# -*- coding: utf-8 -*-


from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


# Блоки контента слева
class ScreenTextBlock_left(models.Model):
    screen = models.ForeignKey('Screens', on_delete=models.CASCADE,
                               related_name='screen_text_block_left')

    text = RichTextField(verbose_name='текст *')
    order = models.IntegerField(default=0, verbose_name='порядковый номер *')

    class Meta:
        verbose_name='блок текста слева'
        verbose_name_plural = 'блоки текста слева'

class ScreenImageBlock_left(models.Model):
    screen = models.ForeignKey('Screens', on_delete=models.CASCADE,
                               related_name='screen_image_block_left')

    image = models.ImageField(upload_to='practicums/blocks/',
                              verbose_name='изображение *')
    order = models.IntegerField(default=0, verbose_name='Порядковый номер *')

    image_desktop_810px = models.ImageField(null=True, blank=True)
    image_desktop_1620px = models.ImageField(null=True, blank=True)
    image_mobile_400px = models.ImageField(null=True, blank=True)
    image_mobile_800px = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name='блок изображения слева'
        verbose_name_plural = 'блоки изображения слева'


class ScreenPopupBlock_left(models.Model):
    screen = models.ForeignKey('Screens', on_delete=models.CASCADE,
                               related_name='screen_popup_block_left')

    menu_title = models.CharField(verbose_name='Заголовок пункта *')
    text = RichTextField(verbose_name='Текст *')
    order = models.IntegerField(default=0, verbose_name='Порядковый номер *')

    class Meta:
        verbose_name='блок выпадающий список слева'
        verbose_name_plural = 'блоки выпадающий список слева'

class ScreenButton_left(models.Model):
    screen = models.ForeignKey('Screens', on_delete=models.CASCADE,
                               related_name='screen_button_block_left')

    button_title = models.CharField(verbose_name='Заголовк кнопки *')

    screen_number = models.IntegerField(default=None,
                                        verbose_name='Номер экрана',
                                        help_text='Укажите номер экрана, на который будет перенаправлять эта кнопка',
                                        null=True, blank=True)

    url = models.URLField(verbose_name='Ссылка', null=True, blank=True)
    pdf_file = models.FileField(
        verbose_name='PDF-файл',
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf']),
        ],  null=True, blank=True
    )

    screen_redirect = models.ForeignKey('Screens', on_delete=models.SET_NULL,
                null=True, blank=True, related_name='redirected_by_button_left')

    order = models.IntegerField(default=0, verbose_name='Порядковый номер *')

    class Meta:
        verbose_name='блок кнопки слева'
        verbose_name_plural = 'блоки кнопок слева'


    def clean(self):
        if not (self.url or self.pdf_file or self.screen_number):
            raise ValidationError('Необходимо заполнить хотя бы одно из полей: "Номер экрана", "Ссылка" или "PDF-файл"')

        if sum(bool(field) for field in [self.url, self.pdf_file, self.screen_number]) > 1:
            raise ValidationError('Можно заполнить только одно из полей: "Номер экрана", "Ссылка" или "PDF-файл"')

    def save(self, *args, **kwargs):
        practicum = self.screen.practicum

        if self.screen_number is not None:
            try:
                screen_redirect = practicum.screens.all()[self.screen_number - 1]
            except IndexError:
                screen_redirect = None
        else:
            screen_redirect = None

        self.screen_redirect = screen_redirect

        super(ScreenButton_left, self).save(*args, **kwargs)



class ScreenTextBlock_right(models.Model):
    screen = models.ForeignKey('Screens', on_delete=models.CASCADE,
                               related_name='screen_text_block_right')

    text = RichTextField(verbose_name='текст *')
    order = models.IntegerField(default=0, verbose_name='порядковый номер *')

    class Meta:
        verbose_name='блок текста справа'
        verbose_name_plural = 'блоки текста справа'

class ScreenImageBlock_right(models.Model):
    screen = models.ForeignKey('Screens', on_delete=models.CASCADE,
                               related_name='screen_image_block_right')

    image = models.ImageField(upload_to='practicums/blocks/',
                              verbose_name='изображение *')
    order = models.IntegerField(default=0, verbose_name='Порядковый номер *')

    image_desktop_810px = models.ImageField(null=True, blank=True)
    image_desktop_1620px = models.ImageField(null=True, blank=True)
    image_mobile_400px = models.ImageField(null=True, blank=True)
    image_mobile_800px = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name='блок изображения справа'
        verbose_name_plural = 'блоки изображения справа'


class ScreenPopupBlock_right(models.Model):
    screen = models.ForeignKey('Screens', on_delete=models.CASCADE,
                               related_name='screen_popup_block_right')

    menu_title = models.CharField(verbose_name='Заголовок пункта *')
    text = RichTextField(verbose_name='Текст *')
    order = models.IntegerField(default=0, verbose_name='Порядковый номер *')

    class Meta:
        verbose_name='блок выпадающий список справа'
        verbose_name_plural = 'блоки выпадающий список справа'

class ScreenButton_right(models.Model):
    screen = models.ForeignKey('Screens', on_delete=models.CASCADE,
                               related_name='screen_button_block_right')

    button_title = models.CharField(verbose_name='Заголовк кнопки *')

    screen_number = models.IntegerField(default=None,
                                        verbose_name='Номер экрана',
                                        help_text='Укажите номер экрана, на который будет перенаправлять эта кнопка',
                                        null=True, blank=True)

    url = models.URLField(verbose_name='Ссылка', null=True, blank=True)
    pdf_file = models.FileField(
        verbose_name='PDF-файл',
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf']),
        ],  null=True, blank=True
    )

    screen_redirect = models.ForeignKey('Screens', on_delete=models.SET_NULL,
                null=True, blank=True, related_name='redirected_by_button_right')

    order = models.IntegerField(default=0, verbose_name='Порядковый номер *')

    class Meta:
        verbose_name='блок кнопки справа'
        verbose_name_plural = 'блоки кнопок справа'


    def clean(self):
        if not (self.url or self.pdf_file or self.screen_number):
            raise ValidationError('Необходимо заполнить хотя бы одно из полей: "Номер экрана", "Ссылка" или "PDF-файл"')

        if sum(bool(field) for field in [self.url, self.pdf_file, self.screen_number]) > 1:
            raise ValidationError('Можно заполнить только одно из полей: "Номер экрана", "Ссылка" или "PDF-файл"')

    def save(self, *args, **kwargs):
        practicum = self.screen.practicum

        if self.screen_number is not None:
            try:
                screen_redirect = practicum.screens.all()[self.screen_number - 1]
            except IndexError:
                screen_redirect = None
        else:
            screen_redirect = None

        self.screen_redirect = screen_redirect

        super(ScreenButton_right, self).save(*args, **kwargs)
