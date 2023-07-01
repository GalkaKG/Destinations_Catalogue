from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic as views


UserModel = get_user_model()


class IndexView(views.TemplateView):
    template_name = 'common/index.html'
    # user = User.objects.filter(username=request.user.username).get()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add extra data to the context
        context['user'] = self.request.user
        return context


# def home_page(request):
#     return render(request, 'common/index.html')


def catalogue(request):
    return render(request, 'common/catalogue.html')

