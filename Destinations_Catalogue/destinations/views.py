from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from Destinations_Catalogue.common.forms import CommentForm
from Destinations_Catalogue.destinations.forms import DestinationCreateForm
from Destinations_Catalogue.destinations.models import Destination


class DestinationCreateView(CreateView):
    template_name = 'destinations/create-destination.html'
    form_class = DestinationCreateForm
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.instance.creator_id = self.request.user.id
        return super().form_valid(form)


class DestinationDetailsView(DetailView):
    model = Destination
    template_name = 'destinations/details-destination.html'
    context_object_name = 'destination'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = self.object.comment_set.all()
        return context

    # destination = Destination.objects.get(id=destination_id)
    # comments = destination.comment_set.all()
    # form = CommentForm()
