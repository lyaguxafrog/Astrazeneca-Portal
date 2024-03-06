# Generated by Django 4.2.8 on 2024-03-06 10:02

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import practics.services.url_valid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Practicum",
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
                (
                    "title",
                    models.CharField(
                        max_length=90, verbose_name="Название практикума *"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="practicum/", verbose_name="Изображение *"
                    ),
                ),
                (
                    "description",
                    ckeditor.fields.RichTextField(
                        help_text="Ограничение в 200 символов.",
                        max_length=200,
                        verbose_name="Описание *",
                    ),
                ),
                (
                    "pacient_description",
                    ckeditor.fields.RichTextField(
                        help_text="Внутри практикума.",
                        verbose_name="Краткая информация о пациенте *",
                    ),
                ),
                (
                    "priority",
                    models.IntegerField(
                        default=50,
                        help_text="Целое число от 1 до 50 включительно.",
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(50),
                        ],
                        verbose_name="Приоритет",
                    ),
                ),
                (
                    "image_desktop_810px",
                    models.ImageField(
                        blank=True, null=True, upload_to="practicum/810px/"
                    ),
                ),
                (
                    "image_desktop_1620px",
                    models.ImageField(
                        blank=True, null=True, upload_to="practicum/1620px/"
                    ),
                ),
                (
                    "image_mobile_400px",
                    models.ImageField(
                        blank=True, null=True, upload_to="practicum/400px/"
                    ),
                ),
                (
                    "image_mobile_800px",
                    models.ImageField(
                        blank=True, null=True, upload_to="practicum/800px/"
                    ),
                ),
                (
                    "speciality",
                    models.ManyToManyField(
                        blank=True,
                        related_name="practicum_speciality",
                        to="pages.specialty",
                        verbose_name="Специальность",
                    ),
                ),
            ],
            options={
                "verbose_name": "практикум",
                "verbose_name_plural": "практикумы",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="ScreenButton",
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
                ("screen_id", models.IntegerField()),
                ("button_title", models.CharField(verbose_name="Заголовк кнопки *")),
                ("side", models.CharField()),
                (
                    "screen_number",
                    models.IntegerField(
                        blank=True,
                        default=None,
                        help_text="Укажите номер экрана, на который будет перенаправлять эта кнопка",
                        null=True,
                        verbose_name="Номер экрана",
                    ),
                ),
                (
                    "url",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        validators=[
                            practics.services.url_valid.validate_relative_or_absolute_url
                        ],
                        verbose_name="Ссылка",
                    ),
                ),
                (
                    "pdf_file",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["pdf"]
                            )
                        ],
                        verbose_name="PDF-файл",
                    ),
                ),
                (
                    "fill_flag",
                    models.BooleanField(default=False, verbose_name="Заливка кнопки."),
                ),
                (
                    "confirmation",
                    models.BooleanField(
                        default=False, verbose_name="Подтверждение действия."
                    ),
                ),
                (
                    "order",
                    models.IntegerField(default=0, verbose_name="Порядковый номер *"),
                ),
            ],
            options={
                "verbose_name": "блок кнопки слева",
                "verbose_name_plural": "блоки кнопок слева",
            },
        ),
        migrations.CreateModel(
            name="ScreenImageBlock",
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
                ("screen_id", models.IntegerField()),
                (
                    "image",
                    models.ImageField(
                        upload_to="practicums/blocks/", verbose_name="изображение *"
                    ),
                ),
                (
                    "order",
                    models.IntegerField(default=0, verbose_name="Порядковый номер *"),
                ),
                ("side", models.CharField()),
                (
                    "image_desktop_810px",
                    models.ImageField(blank=True, null=True, upload_to=""),
                ),
                (
                    "image_desktop_1620px",
                    models.ImageField(blank=True, null=True, upload_to=""),
                ),
                (
                    "image_mobile_400px",
                    models.ImageField(blank=True, null=True, upload_to=""),
                ),
                (
                    "image_mobile_800px",
                    models.ImageField(blank=True, null=True, upload_to=""),
                ),
            ],
            options={
                "verbose_name": "блок изображения слева",
                "verbose_name_plural": "блоки изображения слева",
            },
        ),
        migrations.CreateModel(
            name="ScreenPopupBlock",
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
                ("screen_id", models.IntegerField()),
                ("side", models.CharField()),
                (
                    "order",
                    models.IntegerField(default=0, verbose_name="Порядковый номер *"),
                ),
            ],
            options={
                "verbose_name": "блок выпадающий список слева",
                "verbose_name_plural": "блоки выпадающий список слева",
            },
        ),
        migrations.CreateModel(
            name="ScreenTextBlock",
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
                ("screen_id", models.IntegerField()),
                ("side", models.CharField()),
                ("text", ckeditor.fields.RichTextField(verbose_name="текст *")),
                (
                    "order",
                    models.IntegerField(default=0, verbose_name="порядковый номер *"),
                ),
            ],
            options={
                "verbose_name": "блок текста слева",
                "verbose_name_plural": "блоки текста слева",
            },
        ),
        migrations.CreateModel(
            name="Screens",
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
                (
                    "literature",
                    ckeditor.fields.RichTextField(
                        blank=True, null=True, verbose_name="список литературы"
                    ),
                ),
                (
                    "leterature_approvals_and_decodings",
                    ckeditor.fields.RichTextField(
                        blank=True,
                        null=True,
                        verbose_name="Номер одобрения и расшифровка для списка литературы",
                    ),
                ),
                (
                    "approvals_and_decodings",
                    ckeditor.fields.RichTextField(
                        blank=True,
                        null=True,
                        verbose_name="Номер одобрения и расшифровка",
                    ),
                ),
                (
                    "practicum",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="screens",
                        to="practics.practicum",
                    ),
                ),
            ],
            options={
                "verbose_name": "экран",
                "verbose_name_plural": "экраны",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="PrTest",
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
                (
                    "title",
                    models.CharField(
                        help_text="Ограничение в 60 символов.",
                        max_length=60,
                        verbose_name="Название теста *",
                    ),
                ),
                (
                    "question",
                    ckeditor.fields.RichTextField(verbose_name="Описание задания *"),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="practics/test/", verbose_name="Изображение *"
                    ),
                ),
                (
                    "priority",
                    models.IntegerField(
                        default=50,
                        help_text="Целое число от 1 до 50 включительно.",
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(50),
                        ],
                        verbose_name="Приоритет",
                    ),
                ),
                (
                    "approvals_and_decodings",
                    ckeditor.fields.RichTextField(
                        blank=True,
                        null=True,
                        verbose_name="Номер одобрения и расшифровка",
                    ),
                ),
                (
                    "image_desktop_810px",
                    models.ImageField(
                        blank=True, null=True, upload_to="practics/test/810px"
                    ),
                ),
                (
                    "image_desktop_1620px",
                    models.ImageField(
                        blank=True, null=True, upload_to="practics/test/1620px"
                    ),
                ),
                (
                    "image_mobile_400px",
                    models.ImageField(
                        blank=True, null=True, upload_to="practics/test/400px"
                    ),
                ),
                (
                    "image_mobile_800px",
                    models.ImageField(
                        blank=True, null=True, upload_to="practics/test/800px"
                    ),
                ),
                (
                    "next_test",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="practics.prtest",
                        verbose_name="Следующий тест",
                    ),
                ),
                (
                    "speciality",
                    models.ManyToManyField(
                        blank=True,
                        related_name="prtest_speciality",
                        to="pages.specialty",
                        verbose_name="Специальность",
                    ),
                ),
            ],
            options={
                "verbose_name": "тест",
                "verbose_name_plural": "тесты",
            },
        ),
        migrations.CreateModel(
            name="AnswerButtons",
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
                ("title", models.CharField(verbose_name="Заголовок кнопки *")),
                ("text", ckeditor.fields.RichTextField(verbose_name="Текст *")),
                (
                    "prtest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="buttons",
                        to="practics.prtest",
                    ),
                ),
            ],
            options={
                "verbose_name": "вариант ответа",
                "verbose_name_plural": "варианты ответа",
            },
        ),
    ]
