# Generated by Django 4.2.8 on 2024-03-06 13:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("practics", "0006_rename_questions_prtest_question"),
    ]

    operations = [
        migrations.RenameField(
            model_name="practicum",
            old_name="desription",
            new_name="description",
        ),
    ]