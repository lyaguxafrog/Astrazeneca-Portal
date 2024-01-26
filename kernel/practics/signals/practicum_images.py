# -*- coding: utf-8 -*-

from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from pathlib import Path
from io import BytesIO
from django.core.files import File

from practics.models import Practicum, ScreenImageBlock


class DisableSignals:
    def __init__(self, sender):
        self.sender = sender
        self._receivers = None

    def __enter__(self):
        self._receivers = post_save.receivers
        post_save.receivers = []

    def __exit__(self, exc_type, exc_value, traceback):
        post_save.receivers = self._receivers


target_width_810 = 810
target_width_1620 = 1620
target_width_400 = 400
target_width_800 = 800

@receiver(post_save, sender=Practicum)
def process_practicum(sender, instance, **kwargs):
    if instance.image:
        file_path = instance.image.path

        if Path(file_path).exists():
            with DisableSignals(sender=Practicum):
                image = Image.open(file_path)

                original_width, original_height = image.size

                target_height_810 = int(original_height / original_width * target_width_810)
                target_height_1620 = int(original_height / original_width * target_width_1620)
                target_height_400 = int(original_height / original_width * target_width_400)
                target_height_800 = int(original_height / original_width * target_width_800)

                image_stream_810px = BytesIO()
                image.resize((target_width_810, target_height_810)).save(image_stream_810px, format='WEBP')
                instance.image_desktop_810px.save(f"{instance.image.name}_810px.webp", File(image_stream_810px), save=False)

                image_stream_1620px = BytesIO()
                image.resize((target_width_1620, target_height_1620)).save(image_stream_1620px, format='WEBP')
                instance.image_desktop_1620px.save(f"{instance.image.name}_1620px.webp", File(image_stream_1620px), save=False)

                image_stream_400px = BytesIO()
                image.resize((target_width_400, target_height_400)).save(image_stream_400px, format='WEBP')
                instance.image_mobile_400px.save(f"{instance.image.name}_400px.webp", File(image_stream_400px), save=False)

                image_stream_800px = BytesIO()
                image.resize((target_width_800, target_height_800)).save(image_stream_800px, format='WEBP')
                instance.image_mobile_800px.save(f"{instance.image.name}_800px.webp", File(image_stream_800px), save=False)

                instance.save()

        else:
            print(f"Файл не найден: {file_path}")
