# Generated by Django 4.2.8 on 2024-03-06 08:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("practics", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="practicum",
            name="polymorphic_ctype",
        ),
        migrations.RemoveField(
            model_name="screens",
            name="polymorphic_ctype",
        ),
    ]