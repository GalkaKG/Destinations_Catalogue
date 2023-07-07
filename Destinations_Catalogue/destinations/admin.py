from django.contrib import admin

from Destinations_Catalogue.destinations.models import Destination


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    pass
