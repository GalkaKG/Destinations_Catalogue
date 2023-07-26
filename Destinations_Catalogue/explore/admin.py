from django.contrib import admin

from Destinations_Catalogue.explore.models import Continent, ExploreDestination, Attraction


@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    pass


@admin.register(ExploreDestination)
class ExploreDestinationAdmin(admin.ModelAdmin):
    pass


@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin):
    pass
