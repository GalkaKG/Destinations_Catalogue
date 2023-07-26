from django.shortcuts import render
from django.views.generic import ListView

from Destinations_Catalogue.explore.models import Continent, ExploreDestination


# class ExploreView(ListView):
#     model = Continent
#     template_name = 'explore/explore.html'
#     context_object_name = 'destinations'


def explore(request):
    all_continents = Continent.objects.all()
    all_explore_destinations = ExploreDestination.objects.all().order_by('continent_id')

    context = {
        'continents': all_continents,
        'explore_destinations': all_explore_destinations
    }

    return render(request, 'explore/explore.html', context)
