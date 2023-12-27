from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.db import models

@receiver(m2m_changed, sender=Drug.icons.through)
def validate_icon_count(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action == 'pre_add' and reverse is False:
        if instance.icons.count() + len(pk_set) > 4:
            raise ValidationError('Выбрано слишком много иконок. Выберите не более 4.')
