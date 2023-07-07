from django.db import models
from django.utils import timezone

from Destinations_Catalogue.destinations.models import Destination
from Destinations_Catalogue.profiles.models import CustomUser, ProfileModel


class Comment(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content


# class Like(models.Model):
#     pass
#

# class Favorite(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
#
#     class Meta:
#         unique_together = ('user', 'destination')
#
#     def __str__(self):
#         return f'{self.user.username} - {self.destination.name}'
