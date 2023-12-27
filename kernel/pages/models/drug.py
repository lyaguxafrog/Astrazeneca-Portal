from django.db import models
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField

def validate_icon_count(value):
    if value.count() > 4:
        raise ValidationError('Выбрано слишком много иконок. Выберите не более 4.')

class Drug(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название препарата")
    brief_info = models.TextField(verbose_name="Краткое описание препарата")
    image = models.ImageField(upload_to='drug_images/', verbose_name="Изображение препарата")
    instruction_text = RichTextField(verbose_name="Текст инструкции")
    application_practice = RichTextField(verbose_name="Практика применения")
    approvals_and_decodings = RichTextField(verbose_name="Расшифровки и номера одобрения")
    icons = models.ManyToManyField('Icon', blank=True, related_name='drugs', verbose_name="Иконки")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Препарат'
        verbose_name_plural = 'Препараты'


class Icon(models.Model):
    IMAGE_TYPES = (
        ('image', 'Image'),
        ('svg', 'SVG'),
    )

    drug = models.ForeignKey(Drug, on_delete=models.CASCADE,
                    related_name='icons_set', verbose_name="Препарат")


    image_file = models.FileField(upload_to='icon_files/',
            verbose_name="Иконка",
            help_text="Поддерживаются изображения и SVG", blank=True)

    def __str__(self):
        return str(self.image_file)
