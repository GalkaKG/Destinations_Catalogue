from django.contrib import admin

from Destinations_Catalogue.destinations.models import Destination


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location', 'description', 'price', 'hotel', 'created_at', 'updated_at']
