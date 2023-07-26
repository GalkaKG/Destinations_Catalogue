from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic as views, View
from rest_framework.generics import UpdateAPIView

from Destinations_Catalogue.common.forms import SearchForm, CommentForm, EditCommentForm
from Destinations_Catalogue.common.models import Comment, Favorite, Like
from Destinations_Catalogue.destinations.models import Destination
from .serializers import CommentSerializer

UserModel = get_user_model()


class IndexView(views.FormView):
    template_name = 'common/index.html'
    form_class = SearchForm
    success_url = 'catalogue/'

    def form_valid(self, form):
        search_query = form.cleaned_data['target']
        return redirect(self.get_success_url() + f'?search={search_query}')


def catalogue(request):
    search_query = request.GET.get('search', '')
    destinations = Destination.objects.all().order_by('id')

    # items_per_page = 3  # Number of items to display per page
    # queryset = Destination.objects.all()
    #
    # paginator = Paginator(queryset, items_per_page)
    # page_number = request.GET.get('page')  # Get the page number from the query parameters
    # page_obj = paginator.get_page(page_number)

    if search_query:
        destinations = destinations.filter(name__icontains=search_query)

    context = {
        'destinations': destinations,
        'likes': Like.objects.all(),
        'comments': Comment.objects.all(),
        'form': CommentForm(),
        'search_query': search_query,
        # 'page_obj': page_obj
    }

    user = request.user
    if user.is_authenticated:
        favorites = Favorite.objects.filter(user=user)
        favorite_destinations = favorites.values_list('destination', flat=True)
        context['favorite_destinations'] = favorite_destinations
        liked = Like.objects.filter(user=user)
        liked_destinations = liked.values_list('destination', flat=True)
        context['liked_destinations'] = liked_destinations

    if request.method == "POST":
        form = CommentForm(request.POST)
        if user.is_authenticated:
            form.instance.author = user
            form.instance.destination = Destination.objects.get(id=int(request.POST['destination']))
            if form.is_valid():
                form.save()
                return redirect('catalogue')
        else:
            return redirect('login')

    return render(request, 'common/catalogue.html', context)


class EditCommentAPIView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def put(self, request, *args, **kwargs):
        print(request)
        comment = self.get_object()
        serializer = self.get_serializer(comment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return redirect('catalogue')


def delete_comment(request, pk):
    user = request.user
    comment = Comment.objects.get(id=pk)

    if user.is_authenticated:
        if comment.author_id == user.id:
            comment.delete()
            return redirect('catalogue')
        elif comment.author_id != user.id:
            return render(request, 'error_pages/permission-denied.html')

    return redirect('login')


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


def page_not_found(request, exception):
    return render(request, 'error_pages/404.html')
