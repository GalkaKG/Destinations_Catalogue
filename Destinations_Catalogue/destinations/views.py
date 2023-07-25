from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from Destinations_Catalogue.destinations.forms import DestinationCreateForm, DestinationEditForm
from Destinations_Catalogue.destinations.models import Destination
import requests
import googlemaps
from django.conf import settings


class DestinationCreateView(CreateView):
    template_name = 'destinations/create-destination.html'
    form_class = DestinationCreateForm
    success_url = reverse_lazy('details profile')

    def form_valid(self, form):
        form.instance.creator_id = self.request.user.id
        return super().form_valid(form)


class DestinationDetailsView(DetailView):
    model = Destination
    template_name = 'destinations/details-destination.html'
    context_object_name = 'destination'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comment_set.all()
        destination = self.object
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
        params = {
            'address': f'{destination.name},{destination.location}',
            'key': 'AIzaSyDo2Jl-RLvS0i161gcRVmedZsNtsjLDfGM',
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            location = data['results'][0]['geometry']['location']
            latitude = location['lat']
            longitude = location['lng']
            context['latitude'] = latitude
            context['longitude'] = longitude
            context['address'] = f'{latitude},{longitude}'
        return context


class DestinationEditView(LoginRequiredMixin, UpdateView):
    template_name = 'destinations/edit-destination.html'
    form_class = DestinationEditForm

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return Destination.objects.get(pk=pk)

    def get_success_url(self):
        return reverse_lazy('details destination', kwargs={'pk': self.kwargs.get('pk')})


def options_delete(request, pk):
    destination = Destination.objects.get(id=pk)
    context = {
        'destination': destination
    }

    return render(request, 'destinations/delete-destination.html', context)


@login_required
def delete_destination(request, pk):
    destination = Destination.objects.filter(pk=pk).get()

    if request.user.id == destination.creator_id:
        destination = Destination.objects.filter(pk=pk).get()
        destination.delete()
        return redirect('details profile')

    return render(request, 'error_pages/permission-denied.html')





