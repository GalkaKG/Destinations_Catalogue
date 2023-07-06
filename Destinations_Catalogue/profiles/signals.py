from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ProfileModel, CustomUser


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ProfileModel.objects.create(profile=instance)
