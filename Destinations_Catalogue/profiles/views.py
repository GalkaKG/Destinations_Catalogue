from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordResetView
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from Destinations_Catalogue.common.models import Favorite
from Destinations_Catalogue.destinations.models import Destination
from Destinations_Catalogue.profiles.forms import EditProfileForm, CustomUserCreationForm, ChangePasswordForm, \
    CustomPasswordResetForm
from Destinations_Catalogue.profiles.models import CustomUser, ProfileModel


class ProfileCreateView(CreateView):
    template_name = 'profiles/create-profile.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class CustomLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


def option_logout(request):
    return render(request, 'profiles/logout.html')


def logout_view(request):
    logout(request)
    return redirect('login')


class UserDetailsView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'profiles/details-profile.html'
    context_object_name = 'user'
    login_url = '/profile/login/'

    def get_object(self, queryset=None):
        return self.request.user or None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.user.pk
        current_user = ProfileModel.objects.filter(profile_id=pk).get()
        context['profile'] = current_user
        favorites = Favorite.objects.filter(user=current_user.pk)
        favorite_destinations_id = favorites.values_list('destination', flat=True)
        favorite_destinations = [Destination.objects.filter(id=d).get() for d in favorite_destinations_id]
        context['favorite_destinations'] = favorite_destinations
        created_destinations = Destination.objects.filter(creator_id=current_user.id)
        context['created_destinations'] = created_destinations
        return context


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = ProfileModel
    form_class = EditProfileForm
    template_name = 'profiles/edit-profile.html'
    success_url = reverse_lazy('details profile')

    def get_object(self, queryset=None):
        current_profile = ProfileModel.objects.get(profile_id=self.request.user.pk)
        return current_profile


def option_delete_profile(request):
    return render(request, 'profiles/delete-profile.html')


@login_required
def delete_profile(request):
    request.user.delete()
    return redirect('details profile')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            user = request.user
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            user_changed = user.check_password(old_password)
            if user_changed:
                user.set_password(new_password)
                user.save()
                messages.success(request, "Password changed successfully.")
                return redirect('details profile')
            else:
                messages.error(request, "Old password is incorrect.")
    else:
        form = ChangePasswordForm()
    return render(request, 'profiles/change-password.html', {'form': form})


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'profiles/password-reset-form.html'
