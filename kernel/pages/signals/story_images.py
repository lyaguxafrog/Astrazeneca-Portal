# -*- coding: utf-8 -*-


from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from pathlib import Path
from io import BytesIO
from django.core.files import File

from pages.models import Story


class DisableSignals:
    def __init__(self, sender):
        self.sender = sender
        self._receivers = None

    def __enter__(self):
        self._receivers = post_save.receivers
        post_save.receivers = []

    def __exit__(self, exc_type, exc_value, traceback):
        post_save.receivers = self._receivers

@receiver(post_save, sender=Story)
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

@receiver(post_save, sender=Story)
def process_cover_story(sender, instance, **kwargs):
    if instance.avatar:
        file_path = instance.avatar.path

        if Path(file_path).exists():
            with DisableSignals(sender=Story):
                image = Image.open(file_path)

                original_width, original_height = image.size
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
