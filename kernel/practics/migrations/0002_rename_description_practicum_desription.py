# Generated by Django 4.2.8 on 2024-03-06 12:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("practics", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="practicum",
            old_name="description",
            new_name="desription",
        ),
    ]