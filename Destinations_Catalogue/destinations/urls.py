from django.urls import path, include

from Destinations_Catalogue.common.views import delete_comment, edit_comment
from Destinations_Catalogue.destinations.views import DestinationCreateView, DestinationDetailsView, DestinationEditView

urlpatterns = (
    path('create/', DestinationCreateView.as_view(), name='create destination'),
    path('details/<int:pk>/', DestinationDetailsView.as_view(), name='details destination'),
    path('edit/<int:pk>/', DestinationEditView.as_view(), name='edit destination'),
    path('comment/edit/<int:pk>/', edit_comment, name='edit comment'),
    path('comment/delete/<int:pk>/', delete_comment, name='delete comment'),
)
