from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from Destinations_Catalogue.profiles.forms import EditProfileForm, CustomUserCreationForm
from Destinations_Catalogue.profiles.models import CustomUser, ProfileModel


# UserModel = get_user_model()


class ProfileCreateView(CreateView):
    template_name = 'profiles/create-profile.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class CustomLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class CustomLogoutView(LogoutView, TemplateView, LoginRequiredMixin):
    template_name = 'profiles/logout.html'
    login_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        logout_option = request.POST.get('logout_option')

        if logout_option == 'yes':
            return redirect('home')

        elif logout_option == 'no':
            return redirect('home')

        return super().get(request, *args, **kwargs)


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
        return context


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = ProfileModel
    form_class = EditProfileForm
    template_name = 'profiles/edit-profile.html'
    success_url = reverse_lazy('details profile')

    def get_object(self, queryset=None):
        current_profile = ProfileModel.objects.get(profile_id=self.request.user.pk)
        return current_profile


class ProfileDeleteView(DeleteView):
    model = CustomUser
    template_name = 'profiles/delete-profile.html'
    next_page = reverse_lazy('home')
    # success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, *args, **kwargs):
        self.request.user.delete()
        return redirect('home')
