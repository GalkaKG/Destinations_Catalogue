from django.urls import path
from . import views


urlpatterns = (
    path('create/', views.ProfileCreateView.as_view(), name='profile create'),
    path('details/', views.UserDetailsView.as_view(), name='details profile'),
    path('login/', views.CustomLoginView.as_view(template_name='profiles/login.html'), name='login'),
    path('logout/', views.logout_user, name='logout'),
)
