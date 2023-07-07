from django.urls import path
from . import views
# from .views import CommentCreateView

urlpatterns = (
    path('', views.IndexView.as_view(), name='home'),
    path('catalogue/', views.catalogue, name='catalogue'),
)
