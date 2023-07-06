from django.contrib import admin

from Destinations_Catalogue.profiles.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass
