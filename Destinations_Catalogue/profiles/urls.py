from django.urls import path
from . import views


urlpatterns = (
    path('create/', views.ProfileCreateView.as_view(), name='create profile'),
    path('details/', views.UserDetailsView.as_view(), name='details profile'),
    path('login/', views.CustomLoginView.as_view(template_name='profiles/login.html'), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('edit/', views.CustomEditView.as_view(), name='edit profile'),

)
