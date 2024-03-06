# -*- coding: utf-8 -*-

from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import FileExtensionValidator
from practics.services.url_valid import validate_relative_or_absolute_url


# Блоки контента слева
class ScreenTextBlock(models.Model):
    screen_id = models.IntegerField()

    side = models.CharField()

    text = RichTextField(verbose_name='текст *')
    order = models.IntegerField(default=0, verbose_name='порядковый номер *')

    class Meta:
        verbose_name='блок текста слева'
        verbose_name_plural = 'блоки текста слева'

class ScreenImageBlock(models.Model):
    screen_id = models.IntegerField()

    image = models.ImageField(upload_to='practicums/blocks/',
                              verbose_name='изображение *')
    order = models.IntegerField(default=0, verbose_name='Порядковый номер *')

    side = models.CharField()

    image_desktop_810px = models.ImageField(null=True, blank=True)
    image_desktop_1620px = models.ImageField(null=True, blank=True)
    image_mobile_400px = models.ImageField(null=True, blank=True)
    image_mobile_800px = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name='блок изображения слева'
        verbose_name_plural = 'блоки изображения слева'


class ScreenPopupBlock(models.Model):
    screen_id = models.IntegerField()

    side = models.CharField()

    order = models.IntegerField(default=0, verbose_name='Порядковый номер *')

    class Meta:
        verbose_name='блок выпадающий список слева'
        verbose_name_plural = 'блоки выпадающий список слева'

class PopUpPoint(models.Model):
    PopUpBlockId = models.IntegerField()

    title = models.CharField()
    text = RichTextField()


class ScreenButton(models.Model):
    screen_id = models.IntegerField()

    button_title = models.CharField(verbose_name='Заголовк кнопки *')

    side = models.CharField()

    screen_number = models.IntegerField(default=None,
                                        verbose_name='Номер экрана',
                                        help_text='Укажите номер экрана, на который будет перенаправлять эта кнопка',
                                        null=True, blank=True)

    url = models.CharField(max_length=255, verbose_name='Ссылка',
                    null=True, blank=True,
                    validators=[validate_relative_or_absolute_url])

    pdf_file = models.FileField(
        verbose_name='PDF-файл',
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf']),
        ],  null=True, blank=True
    )

    #screen_redirect = models.ForeignKey('Screens', on_delete=models.SET_NULL,
    #           null=True, blank=True, related_name='redirected_by_button_left')

    fill_flag = models.BooleanField(default=False,
                                    verbose_name='Заливка кнопки.')

    confirmation = models.BooleanField(default=False,
                                    verbose_name='Подтверждение действия.')

    order = models.IntegerField(default=0, verbose_name='Порядковый номер *')

    class Meta:
        verbose_name='блок кнопки слева'
        verbose_name_plural = 'блоки кнопок слева'

    # def clean(self):
    #     if not (self.url or self.pdf_file or self.screen_number):
    #         raise ValidationError('Необходимо заполнить хотя бы одно из полей: "Номер экрана", "Ссылка" или "PDF-файл"')

    #     if sum(bool(field) for field in [self.url, self.pdf_file, self.screen_number]) > 1:
    #         raise ValidationError('Можно заполнить только одно из полей: "Номер экрана", "Ссылка" или "PDF-файл"')

    # def save(self, *args, **kwargs):
    #     practicum = self.screen.practicum

    #     if self.screen_number is not None:
    #         try:
    #             screen_redirect = practicum.screens.all()[self.screen_number - 1]
    #         except IndexError:
    #             screen_redirect = None
    #     else:
    #         screen_redirect = None

    #     self.screen_redirect = screen_redirect

    #     super(ScreenButton, self).save(*args, **kwargs)
