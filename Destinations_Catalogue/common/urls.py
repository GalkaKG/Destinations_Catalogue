from django.urls import path
from . import views


urlpatterns = (
    path('', views.IndexView.as_view(), name='home'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('favorite/<int:pk>/', views.AddFavoriteView.as_view(), name='add favorite'),
    path('like/<int:pk>/', views.LikeView.as_view(), name='like'),
    path('api/edit_comment/<int:pk>/', views.EditCommentAPIView.as_view(), name='edit comment'),
    path('remove_favorite/<int:pk>/', views.RemoveFavoriteView.as_view(), name='remove favorite'),
)



