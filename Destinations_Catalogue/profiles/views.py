from django.contrib.auth import get_user_model, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy

from Destinations_Catalogue.profiles.models import CustomUser

UserModel = get_user_model()


class ProfileCreateView(CreateView):
    model = CustomUser
    template_name = 'profiles/create-profile.html'
    fields = ['username', 'email', 'password']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Assign the user to the profile being created
        form.instance.user = self.request.user

        # Hash the password before saving the user
        form.instance.set_password(form.cleaned_data['password'])
        return super().form_valid(form)


# def details_profile(request):
#     user = User.objects.filter(username=request.user.username).get()
#
#     context = {
#         'user': user
#     }
#
#     return render(request, 'profiles/details-profile.html', context)


class CustomLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


class UserDetailsView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'profiles/details-profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        # Return the profile associated with the currently logged-in user
        return self.request.user
