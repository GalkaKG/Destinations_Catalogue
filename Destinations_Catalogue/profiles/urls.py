from django.urls import path
from . import views


urlpatterns = (
    path('create/', views.ProfileCreateView.as_view(), name='create profile'),
    path('login/', views.CustomLoginView.as_view(template_name='profiles/login.html'), name='login'),
    path('logout/options/', views.option_logout, name='logout options'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.UserDetailsView.as_view(), name='details profile'),
    path('edit/', views.ProfileEditView.as_view(), name='edit profile'),
    path('delete/', views.ProfileDeleteView.as_view(), name='delete profile'),
)
