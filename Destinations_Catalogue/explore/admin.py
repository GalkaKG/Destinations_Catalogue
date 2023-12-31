from django.contrib import admin

from Destinations_Catalogue.explore.models import Continent, ExploreDestination, Attraction


@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    pass


@admin.register(ExploreDestination)
class ExploreDestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'continent']
    ordering = ('continent__name', 'name')


@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin):
    list_display = ['name', 'destination', 'price', 'description']
    ordering = ('destination__name', 'name')
