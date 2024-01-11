# -*- coding: utf-8 -*-

from django.db.models.signals import post_save
from django.dispatch import receiver
from pathlib import Path
from io import BytesIO
from django.core.files import File
from PIL import Image

from pages.models import Events


class DisableSignals:
    def __init__(self, sender):
        self.sender = sender
        self._receivers = None

    def __enter__(self):
        self._receivers = post_save.receivers
        post_save.receivers = []

    def __exit__(self, exc_type, exc_value, traceback):
        post_save.receivers = self._receivers

@receiver(post_save, sender=Events)
def process_event_cover(sender, instance, **kwargs):
    if instance.cover:
        file_path = instance.cover.path

        if Path(file_path).exists():
            with DisableSignals(sender=Events):
                image = Image.open(file_path)

                original_width, original_height = image.size

                target_height_1140 = 1140
                target_height_570 = 570
                target_height_270 = 270
                target_height_540 = 540

                target_width_1140 = int(original_width / original_height * target_height_1140)
                target_width_570 = int(original_width / original_height * target_height_570)
                target_width_270 = int(original_width / original_height * target_height_270)
                target_width_540 = int(original_width / original_height * target_height_540)

                image_stream_570px = BytesIO()
                image.resize((target_width_570, target_height_570)).save(image_stream_570px, format='WEBP')
                instance.image_desktop_570px.save(f"{instance.cover.name}_570px.webp", File(image_stream_570px), save=False)

                image_stream_270px = BytesIO()
                image.resize((target_width_270, target_height_270)).save(image_stream_270px, format='WEBP')
                instance.image_mobile_270px.save(f"{instance.cover.name}_270px.webp", File(image_stream_270px), save=False)

                image_stream_1140px = BytesIO()
                image.resize((target_width_1140, target_height_1140)).save(image_stream_1140px, format='WEBP')
                instance.image_desktop_1140px.save(f"{instance.cover.name}_1140px.webp", File(image_stream_1140px), save=False)

                image_stream_540px = BytesIO()
                image.resize((target_width_540, target_height_540)).save(image_stream_540px, format='WEBP')
                instance.image_mobile_540px.save(f"{instance.cover.name}_540px.webp", File(image_stream_540px), save=False)

                instance.save()
        else:
            print(f"Файл не найден: {file_path}")
