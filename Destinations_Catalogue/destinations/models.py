from django.db import models


class Destination(models.Model):
    name = models.CharField(
        max_length=34,
    )

    description = models.TextField()

    location = models.CharField(
        max_length=34,
    )

    image = models.URLField()

    rating = models.FloatField()

    # category = models.CharField(
    #     max_length=34,
    # )

    price = models.PositiveIntegerField()

