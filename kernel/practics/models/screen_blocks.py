# -*- coding: utf-8 -*-

from django.db import models

from ckeditor.fields import RichTextField
from dynamicadmin.models import Bundle


class BlockEntity(models.Model):
    class Meta:
        abstract = True

    def __str__(self):
        return self.test_1

    test_1 = models.CharField(null=True, blank=True)
    test_2 = models.URLField(null=True, blank=True)

class Block(Bundle):
    test_1 = models.IntegerField(default=0)
    test_2 = RichTextField(null=True, blank=True)
