# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from pages.models import Specialty

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                null=True, blank=True)

    saved_content = models.JSONField(default=dict, null=True)
    temporary_token = models.CharField(null=True, unique=True)
    specialty = models.ForeignKey(Specialty, on_delete=models.SET_NULL,
                            null=True, blank=True, related_name='users')
