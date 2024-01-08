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

                target_height_390 = 390
                target_height_780 = 780
                target_height_1400 = 1400
                target_height_2800 = 2800

                target_width_390 = int(original_width / original_height * target_height_390)
                target_width_780 = int(original_width / original_height * target_height_780)
                target_width_1400 = int(original_width / original_height * target_height_1400)
                target_width_2800 = int(original_width / original_height * target_height_2800)

                image_stream_390px = BytesIO()
                image.resize((target_width_390, target_height_390)).save(image_stream_390px, format='WEBP')
                instance.image_390px.save(f"{instance.cover.name}_390px.webp", File(image_stream_390px), save=False)

                image_stream_780px = BytesIO()
                image.resize((target_width_780, target_height_780)).save(image_stream_780px, format='WEBP')
                instance.image_780px.save(f"{instance.cover.name}_780px.webp", File(image_stream_780px), save=False)

                image_stream_1400px = BytesIO()
                image.resize((target_width_1400, target_height_1400)).save(image_stream_1400px, format='WEBP')
                instance.image_1400px.save(f"{instance.cover.name}_1400px.webp", File(image_stream_1400px), save=False)

                image_stream_2800px = BytesIO()
                image.resize((target_width_2800, target_height_2800)).save(image_stream_2800px, format='WEBP')
                instance.image_2800px.save(f"{instance.cover.name}_2800px.webp", File(image_stream_2800px), save=False)

                instance.save()
        else:
            print(f"Файл не найден: {file_path}")
