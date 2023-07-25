from django.shortcuts import render
from django.views.generic import ListView

from Destinations_Catalogue.destinations.models import Destination


class ExploreView(ListView):
    model = Destination
    template_name = 'explore/explore.html'
    context_object_name = 'destinations'
