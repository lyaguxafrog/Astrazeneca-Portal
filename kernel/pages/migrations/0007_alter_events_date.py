# Generated by Django 4.2.8 on 2023-12-29 08:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0006_alter_story_link_to_page"),
    ]

    operations = [
        migrations.AlterField(
            model_name="events",
            name="date",
            field=models.DateField(verbose_name="Дата мероприятия"),
        ),
    ]
