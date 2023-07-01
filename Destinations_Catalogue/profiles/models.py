from django.db import models
from django.contrib.auth.models import User, AbstractUser


# class CustomUser(AbstractUser):
#     # email = models.EmailField(
#     #     unique=True,
#     # )
#     #
#     AUTH_USER_MODEL = "<THE PATH OF THE USER MODEL>"
#     ...


class ProfileModel(models.Model):
    image = models.URLField(
        blank=True,
        null=True,
    )

    # user = models.OneToOneField(
    #     User,
    #     on_delete=models.CASCADE,
    #     # primary_key=True,
    # )
