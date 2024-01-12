# -*- coding: utf-8 -*-

from django.db.models.signals import post_save, pre_delete, m2m_changed
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType

from pages.models import Articles, Events, VideoLectures, Drug, LastAdds

@receiver(post_save, sender=Articles)
def create_last_adds_articles(sender, instance, created, **kwargs):
    if created:
        last_adds = LastAdds.objects.create(
            content_object=instance,
            content_type_name="article",
            content=instance.article_name
        )

        last_adds.speciality.set(instance.speciality.all())

@receiver(post_save, sender=Events)
def create_last_adds_event(sender, instance, created, **kwargs):
    if created:
        LastAdds.objects.create(content_object=instance,
                                content_type_name="event",
                                content=instance.name)


@receiver(post_save, sender=VideoLectures)
def create_last_adds_video(sender, instance, created, **kwargs):
    if created:
        last_adds = LastAdds.objects.create(
            content_object=instance,
            content_type_name="video",
            content=instance.video_article
        )

        last_adds.speciality.set(instance.speciality.all())


@receiver(post_save, sender=Drug)
def create_last_adds_drug(sender, instance, created, **kwargs):
    if created:
        last_adds = LastAdds.objects.create(
            content_object=instance,
            content_type_name="drug",
            content=instance.name
        )

        last_adds.speciality.set(instance.speciality.all())

@receiver(pre_delete, sender=Articles)
def delete_related_last_adds_article(sender, instance, **kwargs):
    LastAdds.objects.filter(content_type=ContentType.objects.get_for_model(instance), object_id=instance.id).delete()

@receiver(pre_delete, sender=Events)
def delete_related_last_adds_event(sender, instance, **kwargs):
    LastAdds.objects.filter(content_type=ContentType.objects.get_for_model(instance), object_id=instance.id).delete()

@receiver(pre_delete, sender=VideoLectures)
def delete_related_last_adds_video(sender, instance, **kwargs):
    LastAdds.objects.filter(content_type=ContentType.objects.get_for_model(instance), object_id=instance.id).delete()

@receiver(pre_delete, sender=Drug)
def delete_related_last_adds_drug(sender, instance, **kwargs):
    LastAdds.objects.filter(content_type=ContentType.objects.get_for_model(instance), object_id=instance.id).delete()

@receiver(m2m_changed, sender=VideoLectures.speciality.through)
def update_last_adds_speciality_video(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action == 'post_add' or action == 'post_remove':
        last_adds = LastAdds.objects.filter(content_type=ContentType.objects.get_for_model(instance),
                                           object_id=instance.id).first()

        if last_adds:
            last_adds.speciality.set(instance.speciality.all())

@receiver(m2m_changed, sender=VideoLectures.speciality.through)
def update_last_adds_speciality_video(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action == 'post_add' or action == 'post_remove':
        last_adds = LastAdds.objects.filter(content_type=ContentType.objects.get_for_model(instance),
                                           object_id=instance.id).first()

        if last_adds:
            last_adds.speciality.set(instance.speciality.all())

@receiver(m2m_changed, sender=Articles.speciality.through)
def update_last_adds_speciality_video(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action == 'post_add' or action == 'post_remove':
        last_adds = LastAdds.objects.filter(content_type=ContentType.objects.get_for_model(instance),
                                           object_id=instance.id).first()

        if last_adds:
            last_adds.speciality.set(instance.speciality.all())

@receiver(m2m_changed, sender=Drug.speciality.through)
def update_last_adds_speciality_video(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action == 'post_add' or action == 'post_remove':
        last_adds = LastAdds.objects.filter(content_type=ContentType.objects.get_for_model(instance),
                                           object_id=instance.id).first()

        if last_adds:
            last_adds.speciality.set(instance.speciality.all())
