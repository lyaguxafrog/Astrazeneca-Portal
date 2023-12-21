# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _

class SavedByUser(models.Model):
   saved_data = models.TextField()
