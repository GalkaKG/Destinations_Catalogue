from django.urls import path
from . import views


urlpatterns = (
    path('create/', views.ProfileCreateView.as_view(), name='profile create'),
    path('details/', views.details_profile, name='details profile'),
)
