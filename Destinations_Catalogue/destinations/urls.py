from django.urls import path, include

from Destinations_Catalogue.common.views import delete_comment
from Destinations_Catalogue.destinations.views import DestinationCreateView, DestinationDetailsView, \
    DestinationEditView, delete_destination, options_delete, show_map

urlpatterns = (
    path('create/', DestinationCreateView.as_view(), name='create destination'),
    path('details/<int:pk>/', DestinationDetailsView.as_view(), name='details destination'),
    path('edit/<int:pk>/', DestinationEditView.as_view(), name='edit destination'),
    path('options/delete/<int:pk>/', options_delete, name='delete destination options'),
    path('delete/<int:pk>/', delete_destination, name='delete destination'),
    # path('comment/edit/<int:pk>/', edit_comment, name='edit comment'),
    path('comment/delete/<int:pk>/', delete_comment, name='delete comment'),
    path('map/', show_map, name='show map'),
)
