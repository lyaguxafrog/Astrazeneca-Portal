# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image
from django.db.models.signals import pre_save
from django.dispatch import receiver
from pathlib import Path
from io import BytesIO
from django.core.files import File



class Story(models.Model):
    avatar = models.ImageField(upload_to='story_avatars/')
    title = models.CharField(max_length=255)
    content = models.TextField()
    video = models.FileField(upload_to='story_videos/',
                             null=True, blank=True)
    cover_image = models.ImageField(upload_to='story_covers/',
                                    null=True, blank=True)
    link_to_page = models.URLField(null=True, blank=True)
    specialties = models.ManyToManyField('pages.Specialty',
                                         blank=True, null=True)
    is_active = models.BooleanField(default=True)


    avatar_desktop_120px = models.ImageField(null=True, blank=True)
    avatar_desktop_280px = models.ImageField(null=True, blank=True)
    avatar_mobile_70px = models.ImageField(null=True, blank=True)
    avatar_mobile_140px = models.ImageField(null=True, blank=True)

    cover_450px = models.ImageField(null=True, blank=True)
    cover_900px = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Истории'
        verbose_name_plural = 'Истории'

class DisableSignals:
    def __init__(self, sender):
        self.sender = sender
        self._receivers = None

    def __enter__(self):
        self._receivers = pre_save.receivers
        pre_save.receivers = []

    def __exit__(self, exc_type, exc_value, traceback):
        pre_save.receivers = self._receivers

@receiver(pre_save, sender=Story)
def process_avatar_story(sender, instance, **kwargs):
    if instance.avatar:
        file_path = instance.avatar.path

        if Path(file_path).exists():
            with DisableSignals(sender=Story):
                image = Image.open(file_path)

                original_width, original_height = image.size

                target_width_120 = 120
                target_width_280 = 280
                target_width_70 = 70
                target_width_140 = 140

                target_height_120 = int(original_height / original_width * target_width_120)
                target_height_280 = int(original_height / original_width * target_width_280)
                target_height_70 = int(original_height / original_width * target_width_70)
                target_height_140 = int(original_height / original_width * target_width_140)

                image_stream_120px = BytesIO()
                image.resize((target_width_120, target_height_120)).save(image_stream_120px, format='WEBP')
                instance.avatar_desktop_120px.save(f"{instance.avatar.name}_120px.webp", File(image_stream_120px), save=False)

                image_stream_280px = BytesIO()
                image.resize((target_width_280, target_height_280)).save(image_stream_280px, format='WEBP')
                instance.avatar_desktop_280px.save(f"{instance.avatar.name}_280px.webp", File(image_stream_280px), save=False)

                image_stream_70px = BytesIO()
                image.resize((target_width_70, target_height_70)).save(image_stream_70px, format='WEBP')
                instance.avatar_mobile_70px.save(f"{instance.avatar.name}_70px.webp", File(image_stream_70px), save=False)

                image_stream_140px = BytesIO()
                image.resize((target_width_140, target_height_140)).save(image_stream_140px, format='WEBP')
                instance.avatar_mobile_140px.save(f"{instance.avatar.name}_140px.webp", File(image_stream_140px), save=False)


                instance.save()

        else:
            print(f"Файл не найден: {file_path}")


        if instance.cover_image:
            file_path = instance.cover_image.path

            if Path(file_path).exists():
                with DisableSignals(sender=Story):
                    image = Image.open(file_path)

                    original_width, original_height = image.size

                    target_width_450 = 450
                    target_width_900 = 900

                    target_height_450 = int(original_height / original_width * target_width_450)
                    target_height_900 = int(original_height / original_width * target_width_900)

                    image_stream_450px = BytesIO()
                    image.resize((target_width_450, target_height_450)).save(image_stream_450px, format='WEBP')
                    instance.cover_450px.save(f"{instance.cover_image.name}_450px.webp", File(image_stream_450px), save=False)

                    image_stream_900px = BytesIO()
                    image.resize((target_width_900, target_height_900)).save(image_stream_900px, format='WEBP')
                    instance.cover_900px.save(f"{instance.cover_image.name}_450px.webp", File(image_stream_900px), save=False)

                    instance.save()
