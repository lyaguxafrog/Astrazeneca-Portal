# -*- coding: utf-8 -*-


from rest_framework import serializers
from pages.models import Drug, Icon, DrugFAQ
from urllib.parse import urlparse



class DrugListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    image_1400px = serializers.SerializerMethodField()
    image_2800px = serializers.SerializerMethodField()
    image_390px = serializers.SerializerMethodField()
    image_780px = serializers.SerializerMethodField()

    class Meta:
        model = Drug
        fields = [
            'id',
            'name',
            'brief_info',
            'image',
            'image_1400px',
            'image_2800px',
            'image_390px',
            'image_780px',
                  ]

    def get_image_1400px(self, obj):
        return self.get_relative_url(obj.image_1400px)

    def get_image_2800px(self, obj):
        return self.get_relative_url(obj.image_2800px)

    def get_image_390px(self, obj):
        return self.get_relative_url(obj.image_390px)

    def get_image_780px(self, obj):
        return self.get_relative_url(obj.image_780px)

    def get_image(self, obj):
        return obj.image.url if obj.image else None

    def get_relative_url(self, file_field_or_url):
        if file_field_or_url and hasattr(file_field_or_url, 'url'):
            return file_field_or_url.url
        elif isinstance(file_field_or_url, str) and file_field_or_url.startswith('http'):
            return file_field_or_url
        return None

class IconSerializer(serializers.ModelSerializer):
    image_file = serializers.SerializerMethodField()

    class Meta:
        model = Icon
        fields = ['id', 'image_file']

    def get_image_file(self, obj):
        return obj.image_file.url if obj.image_file else None

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugFAQ
        fields = ['title',
                  'text',
                  'order']


class DrugSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    icons = IconSerializer(many=True, read_only=True)
    faq = FAQSerializer(many=True, read_only=True)
    application_practices = serializers.SerializerMethodField()
    image_1400px = serializers.SerializerMethodField()
    image_2800px = serializers.SerializerMethodField()
    image_390px = serializers.SerializerMethodField()
    image_780px = serializers.SerializerMethodField()

    class Meta:
        model = Drug
        fields = '__all__'

    def get_image(self, obj):
        return obj.image.url if obj.image else None

    def get_image_1400px(self, obj):
        return obj.image_1400px.url if obj.image_1400px else None

    def get_image_2800px(self, obj):
        return obj.image_2800px.url if obj.image_2800px else None

    def get_image_390px(self, obj):
        return obj.image_390px.url if obj.image_390px else None

    def get_image_780px(self, obj):
        return obj.image_780px.url if obj.image_780px else None

    def to_representation(self, instance):
        data = super().to_representation(instance)

        # Обработка поля file_field для получения относительного пути
        file_field_url = data.get('file_field')
        if file_field_url:
            parsed_url = urlparse(file_field_url)
            # Оставляем только относительный путь, начиная с /media/
            relative_path = parsed_url.path if parsed_url.path.startswith('/media/') else None
            data['file_field'] = relative_path

        return data

    def get_application_practices(self, obj):
        articles = obj.application_practice_articles.all()
        videos = obj.application_practice_videos.all()

        # Combine articles and videos into a single list
        combined_practices = []
        for article in articles:
            combined_practices.append({
                'id': article.id,
                'type': 'article',
                'image': article.cover.url if article.cover else None,
                'name': article.article_name,
            })

        for video in videos:
            combined_practices.append({
                'id': video.id,
                'type': 'video',
                'image': video.video_cover.url if video.video_cover else None,
                'name': video.video_article,
            })

        return combined_practices
