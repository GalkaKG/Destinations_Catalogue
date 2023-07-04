from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.views.generic import CreateView

from Destinations_Catalogue.destinations.forms import DestinationCreateForm


class DestinationCreateView(CreateView):
    template_name = 'destinations/create-destination.html'
    form_class = DestinationCreateForm
    success_url = reverse_lazy('catalogue')


