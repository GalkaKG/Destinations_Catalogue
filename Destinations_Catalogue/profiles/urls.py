from django.urls import path
from . import views


urlpatterns = (
    path('create/', views.ProfileCreateView.as_view(), name='profile create'),
    path('details/', views.UserDetailsView.as_view(), name='details profile'),
    path('login/', views.LoginView.as_view(), name='login'),
)
