# # -*- coding: utf-8 -*-

# from rest_framework import serializers

# from practics.models import (ScreenPopupBlock_left,
#                              ScreenButton_left, ScreenImageBlock_left,
#                              ScreenTextBlock_left, ScreenButton_right,
#                              ScreenImageBlock_right, ScreenPopupBlock_right,
#                              ScreenTextBlock_right)

# # лево
# class LeftTextSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ScreenTextBlock_left
#         fields = '__all__'

# class LeftImagesSerializer(serializers.ModelSerializer):
#     image_desktop_810px = serializers.SerializerMethodField()
#     image_desktop_1620px = serializers.SerializerMethodField()
#     image_mobile_400px = serializers.SerializerMethodField()
#     image_mobile_800px = serializers.SerializerMethodField()


#     class Meta:
#         model = ScreenImageBlock_left
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


# class LeftPopUpSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ScreenPopupBlock_left
#         fields = '__all__'

# class LeftButtonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ScreenButton_left
#         fields = '__all__'


# # право
# class RightTextSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ScreenTextBlock_right
#         fields = '__all__'

# class RightImagesSerializer(serializers.ModelSerializer):
#     image_desktop_810px = serializers.SerializerMethodField()
#     image_desktop_1620px = serializers.SerializerMethodField()
#     image_mobile_400px = serializers.SerializerMethodField()
#     image_mobile_800px = serializers.SerializerMethodField()


#     class Meta:
#         model = ScreenImageBlock_right
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


# class RightPopUpSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ScreenPopupBlock_right
#         fields = '__all__'

# class RightButtonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ScreenButton_right
#         fields = '__all__'
