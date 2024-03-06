# Generated by Django 4.2.8 on 2024-03-06 10:45

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import pages.models.video_lectures


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_name', models.CharField(help_text='Ограничение в 90 символов', max_length=90, verbose_name='Заголовок *')),
                ('main_cover_desktop', models.ImageField(upload_to='article_cover/', verbose_name='Главная картинка статьи(десктоп) *')),
                ('main_cover_mobile', models.ImageField(upload_to='article_cover/', verbose_name='Главная картинка статьи(мобильная) *')),
                ('cover_desktop', models.ImageField(upload_to='article_covers/', verbose_name='Обложка(десктоп) *')),
                ('cover_mobile', models.ImageField(upload_to='article_cover/', verbose_name='Обложка(мобильная) *')),
                ('first_abzac', ckeditor.fields.RichTextField(verbose_name='Первый абзац *')),
                ('final_content', ckeditor.fields.RichTextField(verbose_name='Заключение *')),
                ('access_number', ckeditor.fields.RichTextField(verbose_name='Поле для добавления расшифровок и номеров одобрения *')),
                ('center_title', models.BooleanField(default=False, help_text='Поставьте галочку, чтобы заголовок отображался по центру обложки', verbose_name='Заголовок по центру')),
                ('priority', models.IntegerField(default=50, help_text='Целое число от 1 до 50 включительно.', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(50)], verbose_name='Приоритет')),
                ('article_type', models.CharField(choices=[('article', 'Статья'), ('innovation', 'Инновация')], max_length=255, verbose_name='Тип статьи *')),
                ('information', ckeditor.fields.RichTextField(verbose_name='текстовый блок для ввода инфы о статьи на разводящей станице статей *')),
                ('cover_desktop_1400px', models.ImageField(blank=True, null=True, upload_to='article_cover/1400px/')),
                ('cover_desktop_2800px', models.ImageField(blank=True, null=True, upload_to='article_cover/2800px/')),
                ('cover_mobile_420px', models.ImageField(blank=True, null=True, upload_to='article_cover/420px/')),
                ('cover_mobile_840px', models.ImageField(blank=True, null=True, upload_to='article_cover/840px/')),
                ('main_cover_desktop_1600px', models.ImageField(blank=True, null=True, upload_to='article_cover/main_cover/')),
                ('main_cover_desktop_3200px', models.ImageField(blank=True, null=True, upload_to='article_cover/main_cover/')),
                ('main_cover_mobile_360px', models.ImageField(blank=True, null=True, upload_to='article_cover/main_cover/')),
                ('main_cover_mobile_720px', models.ImageField(blank=True, null=True, upload_to='article_cover/main_cover/')),
                ('practic_desktop_400px', models.ImageField(blank=True, null=True, upload_to='article_cover/practic/')),
                ('practic_desktop_800px', models.ImageField(blank=True, null=True, upload_to='article_cover/practic/')),
                ('practic_mobile_280px', models.ImageField(blank=True, null=True, upload_to='article_cover/practic/')),
                ('practic_mobile_560px', models.ImageField(blank=True, null=True, upload_to='article_cover/practic/')),
                ('favorite_desktop_300px', models.ImageField(blank=True, null=True, upload_to='article_cover/ffavorites')),
                ('favorite_desktop_600px', models.ImageField(blank=True, null=True, upload_to='article_cover/ffavorites')),
                ('favorite_mobile_250px', models.ImageField(blank=True, null=True, upload_to='article_cover/ffavorites')),
                ('favorite_mobile_500px', models.ImageField(blank=True, null=True, upload_to='article_cover/ffavorites')),
            ],
            options={
                'verbose_name': 'статью',
                'verbose_name_plural': 'статьи',
            },
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ограничение в 90 символов', max_length=90, verbose_name='Название препарата *')),
                ('brief_info', models.TextField(verbose_name='Краткое описание препарата *')),
                ('image_desktop', models.ImageField(upload_to='drug_images/', verbose_name='Изображение препарата для десктопа *')),
                ('image_mobile', models.ImageField(upload_to='drug_images/', verbose_name='Изображение препарата для мобильной *')),
                ('approvals_and_decodings', ckeditor.fields.RichTextField(verbose_name='Расшифровки и номера одобрения *')),
                ('url_field', models.URLField(blank=True, null=True, verbose_name='Ссылка на интрукцию в PDF')),
                ('file_field', models.FileField(blank=True, null=True, upload_to='pdf_files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='Инструкция в формате PDF')),
                ('priority', models.IntegerField(default=50, help_text='Целое число от 1 до 50 включительно.', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(50)], verbose_name='Приоритет')),
                ('image_desktop_1400px', models.ImageField(blank=True, null=True, upload_to='drugs/1400px/', verbose_name='Изображение 1400px')),
                ('image_desktop_700px', models.ImageField(blank=True, null=True, upload_to='drugs/700px/', verbose_name='Изображение 700px')),
                ('image_mobile_270px', models.ImageField(blank=True, null=True, upload_to='drugs/270px/', verbose_name='Изображение 270px')),
                ('image_mobile_540px', models.ImageField(blank=True, null=True, upload_to='drugs/540px/', verbose_name='Изображение 540px')),
                ('favorite_desktop_300px', models.ImageField(blank=True, null=True, upload_to='drugs/ffavorites')),
                ('favorite_desktop_600px', models.ImageField(blank=True, null=True, upload_to='drugs/ffavorites')),
                ('favorite_mobile_250px', models.ImageField(blank=True, null=True, upload_to='drugs/ffavorites')),
                ('favorite_mobile_500px', models.ImageField(blank=True, null=True, upload_to='drugs/ffavorites')),
                ('application_practice_articles', models.ManyToManyField(blank=True, related_name='application_practice_articles', to='pages.articles', verbose_name='Статьи в практике применения')),
            ],
            options={
                'verbose_name': 'препарат',
                'verbose_name_plural': 'препараты',
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название мероприятия *')),
                ('date', models.DateField(verbose_name='Дата окончания мероприятия *')),
                ('cover', models.ImageField(upload_to='event_covers/', verbose_name='Обложка *')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Описание мероприятия(для поиска)')),
                ('url', models.URLField(verbose_name='URL мероприятия *')),
                ('image_desktop_570px', models.ImageField(blank=True, null=True, upload_to='events/570px/')),
                ('image_desktop_1140px', models.ImageField(blank=True, null=True, upload_to='events/1140px/')),
                ('image_mobile_540px', models.ImageField(blank=True, null=True, upload_to='events/270px/')),
                ('image_mobile_270px', models.ImageField(blank=True, null=True, upload_to='events/540px/')),
            ],
            options={
                'verbose_name': 'мероприятие',
                'verbose_name_plural': 'мероприятия',
            },
        ),
        migrations.CreateModel(
            name='MainPageApproveNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', ckeditor.fields.RichTextField(help_text='Существует в едином экземпляре.', verbose_name='Номер одобрения *')),
            ],
            options={
                'verbose_name': 'футер',
                'verbose_name_plural': 'футер',
            },
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название специальности *')),
                ('image', models.ImageField(upload_to='specialty_images/', verbose_name='Изображение *')),
                ('pro', models.CharField(null=True, verbose_name='PRO-')),
            ],
            options={
                'verbose_name': 'специальность',
                'verbose_name_plural': 'специальности',
            },
        ),
        migrations.CreateModel(
            name='VideoLectures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_article', models.CharField(help_text='Ограничение в 90 символов', max_length=90, verbose_name='Заголовок *')),
                ('short_description', models.TextField(verbose_name='Краткое описание *')),
                ('conspect', ckeditor.fields.RichTextField(verbose_name='Конспект видео *')),
                ('video', models.FileField(help_text='Поддерживаются только файлы формата MP4, до 1ГБ.', upload_to='video_lectures/', validators=[pages.models.video_lectures.validate_video_file_size, pages.models.video_lectures.validate_video_file_extension], verbose_name='Видео *')),
                ('video_cover_desktop', models.ImageField(upload_to='video_covers/', verbose_name='Обложка видео, десктоп *')),
                ('video_cover_mobile', models.ImageField(upload_to='video_covers/', verbose_name='Обложка видео, мобильная *')),
                ('access_number', ckeditor.fields.RichTextField(verbose_name='Поле для добавления расшифровок и номеров одобрения *')),
                ('content_type', models.CharField(choices=[('lecture', 'Видеолекция'), ('case', 'Клинические случаи')], max_length=255, verbose_name='Поле для выбора типа контента *  ')),
                ('priority', models.IntegerField(default=50, help_text='Целое число от 1 до 50 включительно.', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(50)], verbose_name='Приоритет')),
                ('video_cover_desktop_1400px', models.ImageField(blank=True, null=True, upload_to='video_covers/1400px/')),
                ('video_cover_desktop_2800px', models.ImageField(blank=True, null=True, upload_to='video_covers/2800px/')),
                ('recomendation_cover_desktop_500px', models.ImageField(blank=True, null=True, upload_to='video_covers/recomendation/')),
                ('recomendation_cover_desktop_1000px', models.ImageField(blank=True, null=True, upload_to='video_covers/recomendation/')),
                ('video_cover_mobile_390px', models.ImageField(blank=True, null=True, upload_to='video_covers/390px/')),
                ('video_cover_mobile_780px', models.ImageField(blank=True, null=True, upload_to='video_covers/780px/')),
                ('video_cover_mobile_420px', models.ImageField(blank=True, null=True, upload_to='video_covers/420px/')),
                ('video_cover_mobile_840px', models.ImageField(blank=True, null=True, upload_to='video_covers/840px/')),
                ('recomendation_cover_mobile_280px', models.ImageField(blank=True, null=True, upload_to='video_covers/recomendation/')),
                ('recomendation_cover_mobile_560px', models.ImageField(blank=True, null=True, upload_to='video_covers/recomendation/')),
                ('practic_desktop_400px', models.ImageField(blank=True, null=True, upload_to='video_covers/practic/')),
                ('practic_desktop_800px', models.ImageField(blank=True, null=True, upload_to='video_covers/practic/')),
                ('practic_mobile_280px', models.ImageField(blank=True, null=True, upload_to='video_covers/practic/')),
                ('practic_mobile_560px', models.ImageField(blank=True, null=True, upload_to='video_covers/practic/')),
                ('favorite_desktop_300px', models.ImageField(blank=True, null=True, upload_to='video_covers/ffavorites')),
                ('favorite_desktop_600px', models.ImageField(blank=True, null=True, upload_to='video_covers/ffavorites')),
                ('favorite_mobile_250px', models.ImageField(blank=True, null=True, upload_to='video_covers/ffavorites')),
                ('favorite_mobile_500px', models.ImageField(blank=True, null=True, upload_to='video_covers/ffavorites')),
                ('drug', models.ManyToManyField(blank=True, null=True, to='pages.drug', verbose_name='Препарат')),
                ('speciality', models.ManyToManyField(to='pages.specialty', verbose_name='Специальность *')),
                ('video_recomendations', models.ManyToManyField(blank=True, null=True, to='pages.videolectures', verbose_name='Видео-рекомендации')),
            ],
            options={
                'verbose_name': 'видео',
                'verbose_name_plural': 'видео',
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='story_avatars/', verbose_name='Аватар *')),
                ('title', models.CharField(max_length=255, verbose_name='Имя *')),
                ('content', models.TextField(verbose_name='Контент *')),
                ('video', models.FileField(upload_to='story_videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])], verbose_name='Видео *')),
                ('cover_image', models.ImageField(upload_to='story_covers/', verbose_name='Обложка *')),
                ('link_to_page', models.URLField(blank=True, null=True, verbose_name='URL на страницу')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активность истории')),
                ('avatar_desktop_120px', models.ImageField(blank=True, null=True, upload_to='')),
                ('avatar_desktop_280px', models.ImageField(blank=True, null=True, upload_to='')),
                ('avatar_mobile_70px', models.ImageField(blank=True, null=True, upload_to='')),
                ('avatar_mobile_140px', models.ImageField(blank=True, null=True, upload_to='')),
                ('cover_450px', models.ImageField(blank=True, null=True, upload_to='')),
                ('cover_900px', models.ImageField(blank=True, null=True, upload_to='')),
                ('specialties', models.ManyToManyField(blank=True, null=True, to='pages.specialty', verbose_name='Специальность')),
            ],
            options={
                'verbose_name': 'историю',
                'verbose_name_plural': 'истории',
            },
        ),
        migrations.CreateModel(
            name='LastAdds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type_name', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('speciality', models.ManyToManyField(blank=True, null=True, related_name='last_adds', to='pages.specialty')),
            ],
        ),
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.FileField(blank=True, help_text='Поддерживаются изображения и SVG', upload_to='icon_files/', verbose_name='Иконка *')),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='icons', to='pages.drug', verbose_name='Препарат')),
            ],
        ),
        migrations.CreateModel(
            name='DrugFAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Заголовок *')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Текст *')),
                ('approvals_and_decodings', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Расшифровки и номера одобрения')),
                ('order', models.PositiveBigIntegerField(verbose_name='Порядковый номер *')),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faq', to='pages.drug')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='drug',
            name='application_practice_videos',
            field=models.ManyToManyField(blank=True, related_name='application_practice_videos', to='pages.videolectures', verbose_name='Видео в практике применения'),
        ),
        migrations.AddField(
            model_name='drug',
            name='speciality',
            field=models.ManyToManyField(to='pages.specialty', verbose_name='Специальность *'),
        ),
        migrations.CreateModel(
            name='ContentBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.CharField(choices=[('text', 'Текст'), ('quote', 'Цитата')], max_length=16, verbose_name='Тип контента *')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст')),
                ('image', models.ImageField(blank=True, null=True, upload_to='content_block_images/', verbose_name='Изображение')),
                ('order', models.PositiveIntegerField(verbose_name='Поорядковый номер *')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_blocks', to='pages.articles')),
            ],
            options={
                'verbose_name': 'блоки контента',
                'verbose_name_plural': 'блоки контента',
            },
        ),
        migrations.AddField(
            model_name='articles',
            name='drug',
            field=models.ManyToManyField(blank=True, to='pages.drug', verbose_name='Препараты'),
        ),
        migrations.AddField(
            model_name='articles',
            name='speciality',
            field=models.ManyToManyField(blank=True, related_name='articles', to='pages.specialty', verbose_name='Специальности'),
        ),
    ]
