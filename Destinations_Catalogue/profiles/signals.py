import os

from django.conf import settings
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import ProfileModel, CustomUser


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ProfileModel.objects.create(profile=instance)


@receiver(pre_delete, sender=ProfileModel)
def delete_file(sender, instance, **kwargs):
    if instance.image:
        path = os.path.join(settings.MEDIA_ROOT, instance.image.name)
        if os.path.isfile(path):
            os.remove(path)
