from django.db import models
from django.utils import timezone

from Destinations_Catalogue.destinations.models import Destination
from Destinations_Catalogue.profiles.models import CustomUser


class Comment(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content
