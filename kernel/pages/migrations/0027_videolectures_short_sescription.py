# Generated by Django 4.2.8 on 2023-12-27 00:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0026_alter_videolectures_content_type_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="videolectures",
            name="short_sescription",
            field=models.TextField(blank=True, verbose_name="Краткое описание"),
        ),
    ]
