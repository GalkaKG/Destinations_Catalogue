from django.db import models


class Continent(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ExploreDestination(models.Model):
    name = models.CharField(max_length=100)
    continent = models.ForeignKey(
        Continent,
        on_delete=models.CASCADE,
        related_name='destinations'
    )
    # description = models.TextField()
    # image = models.ImageField(upload_to='destination_images/')


class Attraction(models.Model):
    name = models.CharField(max_length=100)
    destination = models.ForeignKey(
        ExploreDestination,
        on_delete=models.CASCADE,
        related_name='attractions'
    )
    price = models.FloatField()
    description = models.TextField()
    # image = models.ImageField(upload_to='attraction_images/')
    # Add any other fields relevant to an attraction

    def __str__(self):
        return self.name
