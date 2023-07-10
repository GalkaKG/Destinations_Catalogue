from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic as views, View

from Destinations_Catalogue.common.forms import SearchForm, CommentForm
from Destinations_Catalogue.common.models import Comment, Favorite, Like
from Destinations_Catalogue.destinations.models import Destination

UserModel = get_user_model()


class IndexView(views.TemplateView):
    template_name = 'common/index.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
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
    user = request.user
    form = CommentForm()

    context = {
        'destinations': Destination.objects.all(),
        'likes': Like.objects.all(),
        'form': form
    }

    if user.is_authenticated:
        favorites = Favorite.objects.filter(user=user)
        favorite_destinations = favorites.values_list('destination', flat=True)
        context['favorite_destinations'] = favorite_destinations
        like = Like.objects.filter(user=user)
        liked_destination = like.values_list('destination', flat=True)
        context['liked_destination'] = liked_destination

    if request.method == "POST":
        form = CommentForm(request.POST)
        form.instance.author = request.user
        form.instance.destination = Destination.objects.get(id=int(request.POST['destination']))
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    return render(request, 'common/catalogue.html', context)


class AddFavoriteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        destination_id = self.kwargs.get('pk')
        destination = get_object_or_404(Destination, pk=destination_id)
        is_favorite = Favorite.objects.filter(user=request.user, destination=destination).all()
        if is_favorite:
            is_favorite.delete()
        else:
            Favorite.objects.get_or_create(user=request.user, destination=destination)
        return redirect('catalogue')


class LikeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        destination_id = self.kwargs.get('pk')
        destination = get_object_or_404(Destination, pk=destination_id)
        is_liked = Like.objects.filter(user=request.user, destination=destination).all()
        if is_liked:
            is_liked.delete()
        else:
            Like.objects.get_or_create(user=request.user, destination=destination)
        return redirect('catalogue')

