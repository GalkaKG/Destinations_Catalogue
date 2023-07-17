from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Destinations_Catalogue.common.views import page_not_found


urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('Destinations_Catalogue.common.urls')),
        path('destinations/', include('Destinations_Catalogue.destinations.urls')),
        path('profile/', include('Destinations_Catalogue.profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = page_not_found

