from django.urls import path

from Destinations_Catalogue.explore.views import explore

urlpatterns = (
    path('', explore, name='explore'),
)
