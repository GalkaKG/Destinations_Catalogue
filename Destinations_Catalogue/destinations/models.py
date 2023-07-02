from django.db import models


class Destination(models.Model):
    name = models.CharField(
        max_length=100,
    )
    description = models.TextField()
    location = models.CharField(
        max_length=100,
    )
    image = models.ImageField(
        upload_to='destinations/',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name
