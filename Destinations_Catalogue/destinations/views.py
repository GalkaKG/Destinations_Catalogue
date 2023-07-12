from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

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


class DestinationEditView(LoginRequiredMixin, UpdateView):
    template_name = 'destinations/edit-destination.html'
    form_class = DestinationEditForm
    success_url = reverse_lazy('details profile')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return Destination.objects.get(pk=pk)


def options_delete(request, pk):
    destination = Destination.objects.get(id=pk)
    context = {
        'destination': destination
    }

    return render(request, 'destinations/delete-destination.html', context)


# class DestinationDeleteView(LoginRequiredMixin, DeleteView):
#     # model = Destination
#     template_name = 'destinations/delete-destination.html'
#     success_url = reverse_lazy('details profile')
#     # pk_url_kwarg = 'pk'
#
#     def get_object(self, *args, **kwargs):
#         pk = self.kwargs.get('id')
#         return get_object_or_404(Destination, id=pk)

#     #     return destination.delete()
#
#     def get_object(self, queryset=None):
#         """
#         Retrieves the object to be deleted.
#         """
#
#         # You can customize how the object is retrieved here
#         obj = super().get_object(queryset=queryset)
#         print(queryset)
#         pk = self.kwargs.get('pk')
#         destination = Destination.objects.get(id=pk)
#         destination.delete()
#         return obj


@login_required
def delete_destination(request, pk):
    destination = Destination.objects.filter(pk=pk).get()

    if request.user.id == destination.creator_id:
        destination = Destination.objects.filter(pk=pk).get()
        destination.delete()
        return redirect('details profile')

    return render(request, 'error-messages/permission-denied.html')
