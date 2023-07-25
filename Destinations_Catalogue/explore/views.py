from django.shortcuts import render
from django.views.generic import ListView

from Destinations_Catalogue.explore.models import Continent


class ExploreView(ListView):
    model = Continent
    template_name = 'explore/explore.html'
    context_object_name = 'destinations'
