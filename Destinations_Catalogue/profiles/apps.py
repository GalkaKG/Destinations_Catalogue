from django.apps import AppConfig


# from Destinations_Catalogue.profiles import signals

class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Destinations_Catalogue.profiles'

    def ready(self):
        import Destinations_Catalogue.profiles.signals
