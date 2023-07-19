from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from Destinations_Catalogue.profiles.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        full_admins_group, _ = Group.objects.get_or_create(name='Full Admins')
        limited_admins_group, _ = Group.objects.get_or_create(name='Limited Admins')

    # content_type = ContentType.objects.get_for_model(CustomUser)  # Replace CustomUser with your custom user model
    # all_permissions = Permission.objects.filter(content_type=content_type)
    # full_admins_group.permissions.set(all_permissions)
    # limited_permissions = Permission.objects.filter(content_type=content_type, codename__in=['view_customuser'])
    # limited_admins_group.permissions.set(limited_permissions)
