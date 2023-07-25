from django.urls import path

from Destinations_Catalogue.explore.views import ExploreView

urlpatterns = (
    path('', ExploreView.as_view(), name='explore'),
)
