# Generated by Django 4.2.8 on 2023-12-27 05:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "pages",
            "0036_rename_short_sescription_videolectures_short_description_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="videolectures",
            name="access_number",
            field=ckeditor.fields.RichTextField(
                verbose_name="Поле для добавления расшифровок и номеров одобрения"
            ),
        ),
    ]
