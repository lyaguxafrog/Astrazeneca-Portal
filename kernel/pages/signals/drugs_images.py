# -*- coding: utf-8 -*-

from django.db.models.signals import pre_save
from django.dispatch import receiver
from pathlib import Path
from io import BytesIO
from django.core.files import File
from PIL import Image

from pages.models import Drug


target_width_700 = 700
target_width_1400 = 1400
target_width_270 = 270
target_width_540 = 540
target_width_300 = 300
target_width_600 = 600
target_width_250 = 250
target_width_500 = 500


# блять почему я этим на бекенде занимаюсь
class DisableSignals:
    def __init__(self, sender):
        self.sender = sender
        self._receivers = None

    def __enter__(self):
        self._receivers = pre_save.receivers
        pre_save.receivers = []

    def __exit__(self, exc_type, exc_value, traceback):
        pre_save.receivers = self._receivers

@receiver(pre_save, sender=Drug)
def process_drug_cover(sender, instance, **kwargs):
    if instance.image_desktop:
        file_path = instance.image_desktop.path

        if Path(file_path).exists():
            with DisableSignals(sender=Drug):
                image = Image.open(file_path)

                original_width, original_height = image.size

                target_height_700 = int(original_height / original_width * target_width_700)
                target_height_1400 = int(original_height / original_width * target_width_1400)
                target_height_300 = int(original_width / original_height * target_width_300)
                target_height_600 = int(original_width / original_height * target_width_600)

                image_stream_700px = BytesIO()
                image.resize((target_width_700, target_height_700)).save(image_stream_700px, format='WEBP')
                instance.image_desktop_700px.save(f"{instance.image_desktop.name}_700px.webp", File(image_stream_700px), save=False)

                image_stream_1400px = BytesIO()
                image.resize((target_width_1400, target_height_1400)).save(image_stream_1400px, format='WEBP')
                instance.image_desktop_1400px.save(f"{instance.image_desktop.name}_1400px.webp", File(image_stream_1400px), save=False)

                image_stream_300px = BytesIO()
                image.resize((target_width_300, target_height_300)).save(image_stream_300px, format='WEBP')
                instance.favorite_desktop_300px.save(f"{instance.image_desktop.name}_300px.webp", File(image_stream_300px), save=False)

                image_stream_600px = BytesIO()
                image.resize((target_width_600, target_height_600)).save(image_stream_600px, format='WEBP')
                instance.favorite_desktop_600px.save(f"{instance.image_desktop.name}_600px.webp", File(image_stream_600px), save=False)

                instance.save()
        else:
            print(f"Файл не найден: {file_path}")


        if instance.image_mobile:
            file_path = instance.image_mobile.path

            if Path(file_path).exists():
                with DisableSignals(sender=Drug):
                    image = Image.open(file_path)

                    original_width, original_height = image.size

                    target_height_270 = int(original_height / original_width * target_width_270)
                    target_height_540 = int(original_height / original_width * target_width_540)
                    target_height_250 = int(original_width / original_height * target_width_250)
                    target_height_500 = int(original_width / original_height * target_width_500)


                    image_stream_270px = BytesIO()
                    image.resize((target_width_270, target_height_270)).save(image_stream_270px, format='WEBP')
                    instance.image_mobile_270px.save(f"{instance.image_mobile.name}_270px.webp", File(image_stream_270px), save=False)

                    image_stream_540px = BytesIO()
                    image.resize((target_width_540, target_height_540)).save(image_stream_540px, format='WEBP')
                    instance.image_mobile_540px.save(f"{instance.image_mobile.name}_540px.webp", File(image_stream_540px), save=False)

                    image_stream_500px = BytesIO()
                    image.resize((target_width_500, target_height_500)).save(image_stream_500px, format='WEBP')
                    instance.favorite_mobile_500px.save(f"{instance.image_mobile.name}_500px.webp", File(image_stream_500px), save=False)

                    image_stream_250px = BytesIO()
                    image.resize((target_width_250, target_height_250)).save(image_stream_250px, format='WEBP')
                    instance.favorite_mobile_250px.save(f"{instance.image_mobile.name}_250px.webp", File(image_stream_250px), save=False)


                    instance.save()
