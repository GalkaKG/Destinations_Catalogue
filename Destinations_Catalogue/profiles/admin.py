from django.contrib import admin

from Destinations_Catalogue.profiles.models import CustomUser, ProfileModel


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_filter = ['username', 'is_superuser']


@admin.register(ProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    ordering = ['first_name', 'last_name', 'gender', 'age']
