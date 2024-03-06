# Generated by Django 4.2.8 on 2024-03-06 12:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("practics", "0003_rename_question_prtest_questions"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="practicum",
            name="speciality",
        ),
        migrations.DeleteModel(
            name="ScreenButton",
        ),
        migrations.DeleteModel(
            name="ScreenImageBlock",
        ),
        migrations.DeleteModel(
            name="ScreenPopupBlock",
        ),
        migrations.RemoveField(
            model_name="screens",
            name="practicum",
        ),
        migrations.DeleteModel(
            name="ScreenTextBlock",
        ),
        migrations.DeleteModel(
            name="Practicum",
        ),
        migrations.DeleteModel(
            name="Screens",
        ),
    ]
