from django.db import models
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField

class Icon(models.Model):
    IMAGE_TYPES = (
        ('image', 'Image'),
        ('svg', 'SVG'),
    )

    drug = models.ForeignKey('Drug', on_delete=models.CASCADE,
                    related_name='icons_set', verbose_name="Препарат")

    image_file = models.FileField(upload_to='icon_files/',
            verbose_name="Иконка",
            help_text="Поддерживаются изображения и SVG", blank=True)

    def __str__(self):
        return str(self.image_file)

class Drug(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название препарата")
    brief_info = models.TextField(verbose_name="Краткое описание препарата")
    image = models.ImageField(upload_to='drug_images/', verbose_name="Изображение препарата")
    instruction_text = RichTextField(verbose_name="Текст инструкции")
    application_practice_articles = models.ManyToManyField('pages.Articles', blank=True, related_name='application_practice_articles', verbose_name="Статьи в практике применения")
    application_practice_videos = models.ManyToManyField('pages.VideoLectures', blank=True, related_name='application_practice_videos', verbose_name="Видео в практике применения")
    approvals_and_decodings = RichTextField(verbose_name="Расшифровки и номера одобрения")
    icons = models.ManyToManyField(Icon, blank=True, related_name='drugs', verbose_name="Иконки")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Препарат'
        verbose_name_plural = 'Препараты'
