from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import generic as views, View
from django.views.generic import CreateView, DeleteView, UpdateView

# from .models import Comment, Favorite

from Destinations_Catalogue.common.forms import SearchForm, CommentForm
from Destinations_Catalogue.common.models import Comment
from Destinations_Catalogue.destinations.models import Destination

UserModel = get_user_model()


class IndexView(views.TemplateView):
    template_name = 'common/index.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        # Return the profile associated with the currently logged-in user
        return self.request.user

    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['target']
            google_url = f'https://www.google.com/search?q={search_query}'

            return HttpResponseRedirect(google_url)

        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm
        return context


def catalogue(request):
    context = {
        'destinations': Destination.objects.all()
    }
    return render(request, 'common/catalogue.html', context)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'destinations/details-destination.html'

    def form_valid(self, form):
        destination_id = self.kwargs['destination_id']
        destination = get_object_or_404(Destination, id=destination_id)
        form.instance.destination = destination
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        destination_id = self.kwargs['destination_id']
        return reverse('destination_detail', kwargs={'pk': destination_id})


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'destinations/details-destination.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def get_success_url(self):
        destination_id = self.object.destination.id
        return reverse('destination_detail', kwargs={'pk': destination_id})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'destinations/details-destination.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def get_success_url(self):
        destination_id = self.object.destination.id
        return reverse('details destination', kwargs={'pk': destination_id})


# class ToggleFavoriteView(LoginRequiredMixin, View):
#     def post(self, request, destination_id, *args, **kwargs):
#         destination = get_object_or_404(Destination, id=destination_id)
#         favorite, created = Favorite.objects.get_or_create(user=request.user, destination=destination)
#
#         if created:
#             # Favorite was added
#             # Perform any additional actions or display a success message if needed
#             pass
#         else:
#             # Favorite already existed, so remove it
#             favorite.delete()
#             # Perform any additional actions or display a success message if needed
#
#         # Redirect to the destination detail page or any other desired page
#         return redirect('details destination', pk=destination_id)
