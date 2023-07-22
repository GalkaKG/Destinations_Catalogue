from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, is_staff=False, is_superuser=False):
        if not username:
            raise ValueError("The Username field must be set.")
        user = self.model(username=username, is_staff=is_staff, is_superuser=is_superuser)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)


class CustomUser(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(
        max_length=150,
        unique=True,
    )

    email = models.EmailField(
        unique=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    is_superuser = models.BooleanField(default=False)

    # Specify the field used as the unique identifier for the user
    USERNAME_FIELD = 'username'

    # Here are the fields required for creating a user via the createsuperuser management command.
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class ProfileModel(models.Model):
    CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    first_name = models.CharField(
        max_length=34,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=34,
        blank=True,
        null=True,
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    gender = models.CharField(
        blank=True,
        null=True,
        choices=CHOICES,
    )

    image = models.ImageField(
        # upload_to='destinations/',
        upload_to='profile_pics/',
        blank=True,
        null=True,
    )

    profile = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
    )

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return None

    def __str__(self):
        return f'{self.id} {self.get_full_name()}'

# class Gender(Enum):
#     Male = 'Male'
#     Female = 'Female'
#     Other = 'Other'
#
#     @classmethod
#     def choices(cls):
#         return [(choice.value, choice.name) for choice in cls]
