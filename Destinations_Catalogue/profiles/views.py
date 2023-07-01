from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

UserModel = get_user_model()


def details_profile(request):
    user = User.objects.filter(username=request.user.username).get()

    context = {
        'user': user
    }

    return render(request, 'profiles/details-profile.html', context)


class ProfileCreateView(CreateView):
    model = UserModel
    template_name = 'profiles/create-profile.html'
    fields = ['username', 'password']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Assign the user to the profile being created
        form.instance.user = self.request.user
        return super().form_valid(form)
