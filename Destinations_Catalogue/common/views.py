from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import generic as views
from django.views.generic import CreateView

from .models import Comment

from Destinations_Catalogue.common.forms import SearchForm, CommentForm
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


# def add_comment_to_post(request, pk):
#     post = get_object_or_404(Comment, pk=pk)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.author = request.user  # Assuming you have authentication in place
#             comment.save()
#             return redirect('catalogue')
# return redirect(request.META['HTTP_REFERER'] + f'{post.pk}')
# else:
#     form = CommentForm()
#     return render(request, 'common/catalogue.html', context={'form': form})
#


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'common/comment-create.html'

    def form_valid(self, form):
        # destination_id = self.kwargs['destination']
        #
        # image = Destination.objects.get(id=destination_id)
        # form.instance.author = self.request.user
        #
        # form.instance.destination = image
        # return super().form_valid(form)

        destination_id = self.kwargs['destination_id']
        destination = Destination.objects.get(id=destination_id)
        form.instance.destination = destination
        form.instance.author = self.request.user
        return super().form_valid(form)

    #
    def get_success_url(self):
        image_id = self.kwargs['image_id']
        return redirect('home')
