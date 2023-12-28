# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from pages.models import Specialty

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                null=True, blank=True)

    # Поля для интеграции с SSO
    # sso_user_id = models.CharField(max_length=255, blank=True, null=True, unique=True)
    # access_token = models.CharField(max_length=255, blank=True, null=True)
    # refresh_token = models.CharField(max_length=255, blank=True, null=True)
    # token_expiry = models.DateTimeField(blank=True, null=True)

    saved_content = models.JSONField(default=dict)

    temporary_token = models.CharField(null=True, unique=True)

    specialty = models.ForeignKey(Specialty, on_delete=models.SET_NULL,
                            null=True, blank=True, related_name='users')

    def save_content(self, content_type, content_id):
        if content_type not in self.saved_content:
            self.saved_content[content_type] = []

        if content_id not in self.saved_content[content_type]:
            self.saved_content[content_type].append(content_id)
            self.save()

    def get_saved_content(self, content_type):
        return self.saved_content.get(content_type, [])
