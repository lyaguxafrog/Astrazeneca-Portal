# -*- coding: utf-8 -*-

from pages.models import VideoLectures

from PIL import Image
from django.db.models.signals import pre_save
from django.dispatch import receiver
from pathlib import Path
from io import BytesIO
from django.core.files import File


class DisableSignals:
    def __init__(self, sender):
        self.sender = sender
        self._receivers = None

    def __enter__(self):
        self._receivers = pre_save.receivers
        pre_save.receivers = []

    def __exit__(self, exc_type, exc_value, traceback):
        pre_save.receivers = self._receivers

@receiver(pre_save, sender=VideoLectures)
def process_video_cover(sender, instance, **kwargs):
    if instance.video_cover_desktop:
        file_path = instance.video_cover_desktop.path

        if Path(file_path).exists():
            with DisableSignals(sender=VideoLectures):
                image = Image.open(file_path)

                original_width, original_height = image.size

                target_width_2800 = 2800
                target_width_1400 = 1400
                target_width_430 = 430
                target_width_860 = 860

                target_height_2800 = int(original_height / original_width * target_width_2800)
                target_height_1400 = int(original_height / original_width * target_width_1400)
                target_height_430 = int(original_height / original_width * target_width_430)
                target_height_860 = int(original_height / original_width * target_width_860)

                image_stream_2800px = BytesIO()
                image.resize((target_width_2800, target_height_2800)).save(image_stream_2800px, format='WEBP')
                instance.video_cover_desktop_2800px.save(f"{instance.video_cover_desktop.name}_2800px.webp", File(image_stream_2800px), save=False)

                image_stream_1400px = BytesIO()
                image.resize((target_width_1400, target_height_1400)).save(image_stream_1400px, format='WEBP')
                instance.video_cover_desktop_1400px.save(f"{instance.video_cover_desktop.name}_1400px.webp", File(image_stream_1400px), save=False)

                image_stream_430px = BytesIO()
                image.resize((target_width_430, target_height_430)).save(image_stream_430px, format='WEBP')
                instance.recomendation_cover_desktop_430px.save(f"{instance.video_cover_desktop.name}_430px.webp", File(image_stream_430px), save=False)

                image_stream_860px = BytesIO()
                image.resize((target_width_860, target_height_860)).save(image_stream_860px, format='WEBP')
                instance.recomendation_cover_desktop_860px.save(f"{instance.video_cover_desktop.name}_860px.webp", File(image_stream_860px), save=False)

                instance.save()

        else:
            print(f"Файл не найден: {file_path}")


    if instance.video_cover_mobile:
        file_path = instance.video_cover_mobile.path

        if Path(file_path).exists():
            with DisableSignals(sender=VideoLectures):
                image = Image.open(file_path)

                original_width, original_height = image.size

                target_width_420 = 420
                target_width_840 = 840
                target_width_270 = 270
                target_width_540 = 540

                target_height_420= int(original_height / original_width * target_width_420)
                target_height_840 = int(original_height / original_width * target_width_840)
                target_height_270 = int(original_height / original_width * target_width_270)
                target_height_540 = int(original_height / original_width * target_width_540)

                image_stream_420px = BytesIO()
                image.resize((target_width_420, target_height_420)).save(image_stream_420px, format='WEBP')
                instance.video_cover_mobile_420px.save(f"{instance.video_cover_mobile.name}_420px.webp", File(image_stream_420px), save=False)

                image_stream_840px = BytesIO()
                image.resize((target_width_840, target_height_840)).save(image_stream_840px, format='WEBP')
                instance.video_cover_mobile_840px.save(f"{instance.video_cover_mobile.name}_840px.webp", File(image_stream_840px), save=False)

                image_stream_270x = BytesIO()
                image.resize((target_width_270, target_height_270)).save(image_stream_270x, format='WEBP')
                instance.recomendation_cover_mobile_270px.save(f"{instance.video_cover_mobile.name}_270px.webp", File(image_stream_270x), save=False)

                image_stream_540px = BytesIO()
                image.resize((target_width_540, target_height_540)).save(image_stream_540px, format='WEBP')
                instance.recomendation_cover_desktop_540px.save(f"{instance.video_cover_mobile.name}_540px.webp", File(image_stream_540px), save=False)

                instance.save()

        else:
            print(f"Файл не найден: {file_path}")
