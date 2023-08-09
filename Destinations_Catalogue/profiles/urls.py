from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = (
    path('create/', views.ProfileCreateView.as_view(), name='create profile'),
    path('login/', views.CustomLoginView.as_view(template_name='profiles/login.html'), name='login'),
    path('logout/options/', views.option_logout, name='logout options'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.UserDetailsView.as_view(), name='details profile'),
    path('edit/', views.ProfileEditView.as_view(), name='edit profile'),
    path('delete_profile/options/', views.option_delete_profile, name='delete profile options'),
    path('delete/', views.delete_profile, name='delete profile'),
    path('change_password/', views.change_password, name='change password'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='profiles/reset-confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='profiles/reset-complete.html'), name='password_reset_complete'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(template_name='profiles/reset-done.html'), name='password_reset_done'),
    path('reset_password/', views.CustomPasswordResetView.as_view(), name='reset_password'),
)
