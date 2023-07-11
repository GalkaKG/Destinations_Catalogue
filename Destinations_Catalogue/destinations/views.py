from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from Destinations_Catalogue.destinations.forms import DestinationCreateForm, DestinationEditForm
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
        context['comments'] = self.object.comment_set.all()
        return context


class DestinationEditView(UpdateView):
    template_name = 'destinations/edit-destination.html'
    form_class = DestinationEditForm
    success_url = reverse_lazy('details profile')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return Destination.objects.get(pk=pk)




