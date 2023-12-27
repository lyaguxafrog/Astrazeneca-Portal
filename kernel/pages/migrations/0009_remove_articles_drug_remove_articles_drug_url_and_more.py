# Generated by Django 4.2.8 on 2023-12-26 18:13

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0008_alter_articles_article_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="articles",
            name="drug",
        ),
        migrations.RemoveField(
            model_name="articles",
            name="drug_url",
        ),
        migrations.RemoveField(
            model_name="articles",
            name="quote",
        ),
        migrations.RemoveField(
            model_name="articles",
            name="quote_image",
        ),
        migrations.CreateModel(
            name="Quote",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", ckeditor.fields.RichTextField(blank=True)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="quote_images/"),
                ),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="quotes",
                        to="pages.articles",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="article_images/")),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="pages.articles",
                    ),
                ),
            ],
        ),
    ]
