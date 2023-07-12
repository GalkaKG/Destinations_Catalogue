import os.path

from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import pre_delete


@receiver(pre_delete, sender='destinations.Destination')
def delete_file(sender, instance, **kwargs):
    if instance.image:
        path = os.path.join(settings.MEDIA_ROOT, instance.image.name)
        if os.path.isfile(path):
            os.remove(path)
