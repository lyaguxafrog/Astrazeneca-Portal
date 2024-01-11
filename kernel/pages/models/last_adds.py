# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import pre_save
from django.dispatch import receiver

class LastAdds(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    content_type_name = models.CharField(max_length=255)
    content = models.TextField()

@receiver(pre_save, sender=LastAdds)
def limit_last_adds_records(sender, instance, **kwargs):
    max_records = 12

    # Check the number of existing records
    existing_records_count = LastAdds.objects.count()

    # If the limit is reached, delete the oldest record
    if existing_records_count >= max_records:
        oldest_record = LastAdds.objects.order_by('id').first()
        if oldest_record:
            oldest_record.delete()
