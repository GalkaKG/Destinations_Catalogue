from django.urls import path
from . import views
from .views import CommentCreateView

urlpatterns = (
    # path('', views.home_page, name='home'),
    path('', views.IndexView.as_view(), name='home'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('destination/<int:pk>/comment/', CommentCreateView.as_view(), name='create comment'),
)
