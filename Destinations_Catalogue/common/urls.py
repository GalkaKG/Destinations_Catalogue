from django.urls import path
from . import views
# from .views import CommentCreateView

urlpatterns = (
    path('', views.IndexView.as_view(), name='home'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('favorite/<int:pk>/', views.AddFavoriteView.as_view(), name='add favorite'),
    path('like/<int:pk>/', views.LikeView.as_view(), name='like')
)
