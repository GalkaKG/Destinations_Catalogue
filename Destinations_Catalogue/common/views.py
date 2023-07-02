from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic as views


UserModel = get_user_model()


class IndexView(views.TemplateView):
    template_name = 'common/index.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        # Return the profile associated with the currently logged-in user
        return self.request.user


def catalogue(request):
    return render(request, 'common/catalogue.html')

