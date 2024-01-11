# -*- coding: utf-8 -*-

from pages.models import VideoLectures

from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from pathlib import Path
from io import BytesIO
from django.core.files import File


class DisableSignals:
    def __init__(self, sender):
        self.sender = sender
        self._receivers = None

    def __enter__(self):
        self._receivers = post_save.receivers
        post_save.receivers = []

    def __exit__(self, exc_type, exc_value, traceback):
        post_save.receivers = self._receivers

@receiver(post_save, sender=VideoLectures)
def process_video_cover(sender, instance, **kwargs):
    if instance.video_cover_desktop:
        file_path = instance.video_cover_desktop.path

        if Path(file_path).exists():
            with DisableSignals(sender=VideoLectures):
                image = Image.open(file_path)

                original_width, original_height = image.size

                target_width_2800 = 2800
                target_width_1400 = 1400
                target_width_500 = 500
                target_width_1000 = 1000

                target_height_2800 = int(original_height / original_width * target_width_2800)
                target_height_1400 = int(original_height / original_width * target_width_1400)
                target_height_500 = int(original_height / original_width * target_width_500)
                target_height_1000 = int(original_height / original_width * target_width_1000)

                image_stream_2800px = BytesIO()
                image.resize((target_width_2800, target_height_2800)).save(image_stream_2800px, format='WEBP')
                instance.video_cover_desktop_2800px.save(f"{instance.video_cover_desktop.name}_2800px.webp", File(image_stream_2800px), save=False)

                image_stream_1400px = BytesIO()
                image.resize((target_width_1400, target_height_1400)).save(image_stream_1400px, format='WEBP')
                instance.video_cover_desktop_1400px.save(f"{instance.video_cover_desktop.name}_1400px.webp", File(image_stream_1400px), save=False)

                image_stream_500px = BytesIO()
                image.resize((target_width_500, target_height_500)).save(image_stream_500px, format='WEBP')
                instance.recomendation_cover_desktop_500px.save(f"{instance.video_cover_desktop.name}_500px.webp", File(image_stream_500px), save=False)

                image_stream_1000px = BytesIO()
                image.resize((target_width_1000, target_height_1000)).save(image_stream_1000px, format='WEBP')
                instance.recomendation_cover_desktop_1000px.save(f"{instance.video_cover_desktop.name}_1000px.webp", File(image_stream_1000px), save=False)

                instance.save()

        else:
            print(f"Файл не найден: {file_path}")

@receiver(post_save, sender=VideoLectures)
def process_video_mobile_cover(sender, instance, **kwargs):
    if instance.video_cover_mobile:
        file_path = instance.video_cover_mobile.path

        if Path(file_path).exists():
            with DisableSignals(sender=VideoLectures):
                image = Image.open(file_path)

                original_width, original_height = image.size

                target_width_420 = 420
                target_width_840 = 840
                target_width_280 = 280
                target_width_560 = 560
                target_width_390 = 390
                target_width_780 = 780

                target_height_420= int(original_height / original_width * target_width_420)
                target_height_840 = int(original_height / original_width * target_width_840)
                target_height_280 = int(original_height / original_width * target_width_280)
                target_height_560 = int(original_height / original_width * target_width_560)
                target_width_390 = int(original_height / original_width * target_width_390)
                target_height_780 = int(original_height / original_width * target_width_780)



                image_stream_420px = BytesIO()
                image.resize((target_width_420, target_height_420)).save(image_stream_420px, format='WEBP')
                instance.video_cover_mobile_420px.save(f"{instance.video_cover_mobile.name}_420px.webp", File(image_stream_420px), save=False)

                image_stream_840px = BytesIO()
                image.resize((target_width_840, target_height_840)).save(image_stream_840px, format='WEBP')
                instance.video_cover_mobile_840px.save(f"{instance.video_cover_mobile.name}_840px.webp", File(image_stream_840px), save=False)

                image_stream_280x = BytesIO()
                image.resize((target_width_280, target_height_280)).save(image_stream_280x, format='WEBP')
                instance.recomendation_cover_mobile_280px.save(f"{instance.video_cover_mobile.name}_280px.webp", File(image_stream_280x), save=False)

                image_stream_560px = BytesIO()
                image.resize((target_width_560, target_height_560)).save(image_stream_560px, format='WEBP')
                instance.recomendation_cover_mobile_560px.save(f"{instance.video_cover_mobile.name}_560px.webp", File(image_stream_560px), save=False)

                image_stream_390px = BytesIO()
                image.resize((target_width_390, target_width_390)).save(image_stream_390px, format='WEBP')
                instance.video_cover_mobile_390px.save(f"{instance.video_cover_mobile.name}_390px.webp", File(image_stream_390px), save=False)

                image_stream_780px = BytesIO()
                image.resize((target_width_780, target_height_780)).save(image_stream_780px, format='WEBP')
                instance.video_cover_mobile_780px.save(f"{instance.video_cover_mobile.name}_780px.webp", File(image_stream_780px), save=False)

                instance.save()

        else:
            print(f"Файл не найден: {file_path}")
