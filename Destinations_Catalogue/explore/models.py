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
    image = models.ImageField(upload_to='explore/')

    def __str__(self):
        return self.name


class Attraction(models.Model):
    name = models.CharField(max_length=100)
    destination = models.ForeignKey(
        ExploreDestination,
        on_delete=models.CASCADE,
        related_name='attractions'
    )
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='attraction_images/')

    def __str__(self):
        return self.name
