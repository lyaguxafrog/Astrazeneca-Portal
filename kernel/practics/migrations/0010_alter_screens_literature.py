# Generated by Django 4.2.8 on 2024-03-07 13:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("practics", "0009_alter_practicum_priority"),
    ]

    operations = [
        migrations.AlterField(
            model_name="screens",
            name="literature",
            field=models.CharField(
                blank=True, null=True, verbose_name="список литературы"
            ),
        ),
    ]
