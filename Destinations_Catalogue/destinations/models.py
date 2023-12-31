from django.db import models
from Destinations_Catalogue.profiles.models import CustomUser


class Destination(models.Model):
    name = models.CharField(max_length=100,)
    location = models.CharField(max_length=100,)
    description = models.TextField()
    image = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True,)
    creator = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

