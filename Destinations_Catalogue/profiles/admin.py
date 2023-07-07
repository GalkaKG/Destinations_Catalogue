from django.contrib import admin

from Destinations_Catalogue.profiles.models import CustomUser, ProfileModel


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(ProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    pass
