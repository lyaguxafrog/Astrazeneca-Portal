# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saved_content = models.JSONField(default=dict)

    def save_content(self, content_type, content_id):
        if content_type not in self.saved_content:
            self.saved_content[content_type] = []

        if content_id not in self.saved_content[content_type]:
            self.saved_content[content_type].append(content_id)
            self.save()

    def get_saved_content(self, content_type):
        return self.saved_content.get(content_type, [])
