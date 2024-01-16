# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


def validate_video_file_size(value):
    filesize = value.size
    if filesize > 1024 * 1024 * 1024:  # 1 GB
        raise ValidationError(_('Размер файла не должен превышать 1 ГБ.'))

def validate_video_file_extension(value):
    allowed_extensions = ['.mp4']
    if not value.name.lower().endswith(tuple(allowed_extensions)):
        raise ValidationError(_('Разрешены только файлы с расширением .mp4.'))


class VideoLectures(models.Model):
    VIDEO_TYPE_CHOICES = [
        ('lecture', 'Видеолекция'),
        ('case', 'Клинические случаи'),
    ]

    video_article = models.CharField(max_length=90, verbose_name="Заголовок *",
                                     help_text='Ограничение в 90 символов')
    short_description = models.TextField(verbose_name='Краткое описание *')
    conspect = RichTextField(verbose_name="Конспект видео *")
    video = models.FileField(
        upload_to='video_lectures/',
        validators=[validate_video_file_size, validate_video_file_extension],
        verbose_name='Видео *',
        help_text='Поддерживаются только файлы формата MP4, до 1ГБ.'
            )
    video_cover_desktop = models.ImageField(upload_to='video_covers/', verbose_name="Обложка видео, десктоп *")
    video_cover_mobile = models.ImageField(upload_to='video_covers/', verbose_name="Обложка видео, мобильная *")
    drug = models.ManyToManyField("pages.Drug", blank=True, null=True, verbose_name='Препарат')
    video_recomendations = models.ManyToManyField('VideoLectures', null=True, blank=True,
                                            verbose_name='Видео-рекомендации')
    access_number = RichTextField(verbose_name="Поле для добавления расшифровок и номеров одобрения *")
    speciality = models.ManyToManyField("pages.Specialty", verbose_name='Специальность *')
    content_type = models.CharField(max_length=255, choices=VIDEO_TYPE_CHOICES, verbose_name="Поле для выбора типа контента *  ")

    priority = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(50)],
        verbose_name="Приоритет",
        default=50,
        help_text='Целое число от 1 до 50 включительно.'
    )

    video_cover_desktop_1400px = models.ImageField(upload_to='video_covers/1400px/', null=True, blank=True)
    video_cover_desktop_2800px = models.ImageField(upload_to='video_covers/2800px/', null=True, blank=True)
    recomendation_cover_desktop_500px = models.ImageField(upload_to='video_covers/recomendation/', null=True, blank=True)
    recomendation_cover_desktop_1000px = models.ImageField(upload_to='video_covers/recomendation/', null=True, blank=True)

    video_cover_mobile_390px = models.ImageField(upload_to='video_covers/390px/', null=True, blank=True)
    video_cover_mobile_780px = models.ImageField(upload_to='video_covers/780px/', null=True, blank=True)
    video_cover_mobile_420px = models.ImageField(upload_to='video_covers/420px/', null=True, blank=True)
    video_cover_mobile_840px = models.ImageField(upload_to='video_covers/840px/', null=True, blank=True)
    recomendation_cover_mobile_280px = models.ImageField(upload_to='video_covers/recomendation/', null=True, blank=True)
    recomendation_cover_mobile_560px = models.ImageField(upload_to='video_covers/recomendation/', null=True, blank=True)

    practic_desktop_400px = models.ImageField(null=True, blank=True,
        upload_to='video_covers/practic/')
    practic_desktop_800px = models.ImageField(null=True, blank=True,
        upload_to='video_covers/practic/')
    practic_mobile_280px = models.ImageField(null=True, blank=True,
        upload_to='video_covers/practic/')
    practic_mobile_560px = models.ImageField(null=True, blank=True,
        upload_to='video_covers/practic/')

    favorite_desktop_300px = models.ImageField(upload_to='video_covers/ffavorites',
            null=True, blank=True)
    favorite_desktop_600px = models.ImageField(upload_to='video_covers/ffavorites',
            null=True, blank=True)
    favorite_mobile_250px = models.ImageField(upload_to='video_covers/ffavorites',
            null=True, blank=True)
    favorite_mobile_500px = models.ImageField(upload_to='video_covers/ffavorites',
            null=True, blank=True)

    class Meta:
        verbose_name = 'видео'
        verbose_name_plural = 'видео'

    def __str__(self):
        return self.video_article
