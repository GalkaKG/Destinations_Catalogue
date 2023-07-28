from django.urls import path

from Destinations_Catalogue.explore.views import explore, ShowAttractionsView

urlpatterns = (
    path('', explore, name='explore'),
    path('attractions/<int:pk>', ShowAttractionsView.as_view(), name='attraction'),
)
