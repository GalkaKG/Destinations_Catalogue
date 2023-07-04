from django.urls import path, include

from Destinations_Catalogue.destinations.views import DestinationCreateView

urlpatterns = (
    path('create/', DestinationCreateView.as_view(), name='create destination'),
)
