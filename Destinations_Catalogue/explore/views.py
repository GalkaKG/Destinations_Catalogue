from django.shortcuts import render
from django.views import generic

from Destinations_Catalogue.explore.models import Continent, ExploreDestination, Attraction


def explore(request):
    all_continents = Continent.objects.all()
    all_explore_destinations = ExploreDestination.objects.all()

    context = {
        'continents': all_continents,
        'explore_destinations': all_explore_destinations
    }

    return render(request, 'explore/explore.html', context)


class ShowAttractionsView(generic.View):
    template_name = 'explore/attractions.html'

    def get(self, request, *args, **kwargs):
        destination_id = kwargs.get('pk')
        destination_name = ExploreDestination.objects.get(id=destination_id).name
        attractions = Attraction.objects.filter(destination_id=destination_id).all()

        context = {
            'attractions': attractions,
            'destination': destination_name
        }
        return render(request, self.template_name, context)
