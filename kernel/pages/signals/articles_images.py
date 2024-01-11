# -*- coding: utf-8 -*-


from django.db.models.signals import post_save
from django.dispatch import receiver
from pathlib import Path
from io import BytesIO
from django.core.files import File
from PIL import Image
from inflection import ordinal

from pages.models import Articles


target_height_420 = 420
target_height_840 = 840
target_height_1400 = 1400
target_height_2800 = 2800
target_height_1600 = 1600
target_height_3200 = 3200
target_height_360 = 360
target_height_720 = 720

class DisableSignals:
    def __init__(self, sender):
        self.sender = sender
        self._receivers = None

    def __enter__(self):
        self._receivers = post_save.receivers
        post_save.receivers = []

    def __exit__(self, exc_type, exc_value, traceback):
        post_save.receivers = self._receivers

@receiver(post_save, sender=Articles)
def process_articles_mobile_cover(sender, instance, **kwargs):
    if instance.cover_mobile:
        file_path = instance.cover_mobile.path

        if Path(file_path).exists():
            with DisableSignals(sender=Articles):
                image = Image.open(file_path)

                original_width, original_height = image.size

                target_width_420 = int(original_width / original_height * target_height_420)
                target_width_840 = int(original_width / original_height * target_height_840)

                image_stream_420px = BytesIO()
                image.resize((target_width_420, target_height_420)).save(image_stream_420px, format='WEBP')
                instance.cover_mobile_420px.save(f"{instance.cover_mobile.name}_420px.webp", File(image_stream_420px), save=False)

                image_stream_840px = BytesIO()
                image.resize((target_width_840, target_height_840)).save(image_stream_840px, format='WEBP')
                instance.cover_mobile_840px.save(f"{instance.cover_mobile.name}_840px.webp", File(image_stream_840px), save=False)

                instance.save()
        else:
            print(f"Файл не найден: {file_path}")

@receiver(post_save, sender=Articles)
def process_articles_desktop_cover(sender, instance, **kwargs):
    if instance.cover_desktop:
        file_path = instance.cover_desktop.path

        if Path(file_path).exists():
            with DisableSignals(sender=Articles):
                image = Image.open(file_path)

                original_width, ordinal_height = image.size

                target_widht_2800 = int(original_width / ordinal_height * target_height_2800)
                target_widht_1400 = int(original_width / ordinal_height * target_height_1400)

                image_stream_2800px = BytesIO()
                image.resize((target_widht_2800, target_height_2800)).save(image_stream_2800px, format='WEBP')
                instance.cover_desktop_2800px.save(f"{instance.cover_desktop.name}_2800px.webp", File(image_stream_2800px), save=False)

                image_stream_1400px = BytesIO()
                image.resize((target_widht_1400, target_height_1400)).save(image_stream_1400px, format='WEBP')
                instance.cover_desktop_1400px.save(f"{instance.cover_desktop.name}_1400px.webp", File(image_stream_1400px), save=False)

                instance.save()

        else:
            print(f"Файл не найден: {file_path}")


@receiver(post_save, sender=Articles)
def process_article_main_cover_desktop(sender, instance, **kwargs):
    if instance.main_cover_desktop:
        file_path = instance.main_cover_desktop.path

        if Path(file_path).exists():
            with DisableSignals(sender=Articles):
                image = Image.open(file_path)

                original_width, ordinal_height = image.size
                target_wight_1600px = int(original_width / ordinal_height * target_height_1600)
                target_wight_3200px = int(original_width / ordinal_height * target_height_3200)

                image_stream_1600px = BytesIO()
                image.resize((target_wight_1600px, target_height_1600)).save(image_stream_1600px, format='WEBP')
                instance.main_cover_desktop_1600px.save(f"{instance.main_cover_desktop.name}_1600px.webp", File(image_stream_1600px), save=False)

                image_stream_3200px = BytesIO()
                image.resize((target_wight_3200px, target_height_3200)).save(image_stream_3200px, format='WEBP')
                instance.main_cover_desktop_3200px.save(f"{instance.main_cover_desktop.name}_3200px.webp", File(image_stream_3200px), save=False)

                instance.save()

        else:
            print(f"Файл не найден: {file_path}")

@receiver(post_save, sender=Articles)
def process_article_main_cover_mobile(sender, instance, **kwargs):
    if instance.main_cover_mobile:
        file_path = instance.main_cover_mobile.path

        if Path(file_path).exists():
            with DisableSignals(sender=Articles):
                image = Image.open(file_path)

                original_width, ordinal_height = image.size
                target_wight_360px = int(original_width / ordinal_height * target_height_360)
                target_wight_720px = int(original_width / ordinal_height * target_height_720)

                image_stream_360px = BytesIO()
                image.resize((target_wight_360px, target_height_360)).save(image_stream_360px, format='WEBP')
                instance.main_cover_mobile_360px.save(f"{instance.main_cover_mobile.name}_360px", File(image_stream_360px), save=False)

                image_stream_720px = BytesIO()
                image.resize((target_wight_720px, target_height_720)).save(image_stream_720px, format='WEBP')
                instance.main_cover_mobile_720px.save(f"{instance.main_cover_mobile.name}_720px", File(image_stream_720px), save=False)

                instance.save()

        else:
            print(f"Файл не найден: {file_path}")