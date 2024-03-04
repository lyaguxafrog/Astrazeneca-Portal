# # -*- coding: utf-8 -*-

# from rest_framework import serializers

from practics.models import (Practicum, Screens)
from .screen_blocks import (ButtonSerializer, ImagesSerializer,
                                  PopUpSerializer, TextSerializer)


# Экраны
class ScreenSerializer(serializers.ModelSerializer):
    # лево
    screen_text_block = TextSerializer(many=True, read_only=True)
    screen_image_block = ImagesSerializer(many=True, read_only=True)
    screen_popup_block = PopUpSerializer(many=True, read_only=True)
    screen_button_block = ButtonSerializer(many=True, read_only=True)


#     class Meta:
#         model = Screens
#         fields = '__all__'


# # Практикум


# class PracticumSerializer(serializers.ModelSerializer):
#     screens = ScreenSerializer(many=True, read_only=True)

#     image_desktop_810px = serializers.SerializerMethodField()
#     image_desktop_1620px = serializers.SerializerMethodField()
#     image_mobile_400px = serializers.SerializerMethodField()
#     image_mobile_800px = serializers.SerializerMethodField()

#     class Meta:
#         model = Practicum
#         fields = '__all__'

#     def get_image_desktop_810px(self, obj):
#         return self.get_relative_url(obj.image_desktop_810px)

#     def get_image_desktop_1620px(self, obj):
#         return self.get_relative_url(obj.image_desktop_1620px)

#     def get_image_mobile_400px(self, obj):
#         return self.get_relative_url(obj.image_mobile_400px)

#     def get_image_mobile_800px(self, obj):
#         return self.get_relative_url(obj.image_mobile_800px)

#     def get_relative_url(self, file_field_or_url):
#         if file_field_or_url and hasattr(file_field_or_url, 'url'):
#             return file_field_or_url.url
#         elif isinstance(file_field_or_url,
#         str) and file_field_or_url.startswith('http'):
#             return file_field_or_url
#         return None


# class PracticumListSerializer(serializers.ModelSerializer):
#     screens = ScreenSerializer(many=True, read_only=True)

#     class Meta:
#         model = Practicum
#         fields = '__all__'

#     image_desktop_810px = serializers.SerializerMethodField()
#     image_desktop_1620px = serializers.SerializerMethodField()
#     image_mobile_400px = serializers.SerializerMethodField()
#     image_mobile_800px = serializers.SerializerMethodField()

#     def get_image_desktop_810px(self, obj):
#         return self.get_relative_url(obj.image_desktop_810px)

#     def get_image_desktop_1620px(self, obj):
#         return self.get_relative_url(obj.image_desktop_1620px)

#     def get_image_mobile_400px(self, obj):
#         return self.get_relative_url(obj.image_mobile_400px)

#     def get_image_mobile_800px(self, obj):
#         return self.get_relative_url(obj.image_mobile_800px)

#     def get_relative_url(self, file_field_or_url):
#         if file_field_or_url and hasattr(file_field_or_url, 'url'):
#             return file_field_or_url.url
#         elif isinstance(file_field_or_url,
#         str) and file_field_or_url.startswith('http'):
#             return file_field_or_url
#         return None
