from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from customers.models import Client

USER_ROLES = [
    ('Admin', 'Admin'), 
    ('Staff', 'Staff'),
    ('Driver', 'Driver'),
    ('Tout', 'Tout'),
    ]


# Define a custom user manager
class UserAccountManager(UserManager):
    # override create user method to accept email as username
    def create_user(self, email=None, password=None, **extra_fields):
        return super().create_user(
            email,
            email=email,
            password=password,
            **extra_fields
        )

    # override createsuperuser method to accept email as username
    def create_superuser(self, email=None, password=None, **extra_fields):
        return super().create_superuser(
            email,
            email=email,
            password=password,
            **extra_fields
        )


# define our custom user model
class UserAccount(AbstractUser):
    username = None
    organization = models.ForeignKey(Client, related_name='users', on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    employee_id = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=40, choices=USER_ROLES, default='Staff')

    USERNAME_FIELD = 'email'


    REQUIRED_FIELDS = []

    objects = UserAccountManager()

    class Meta:
        ordering = ['-date_joined']


class Staff(models.Model):
    pass

class Role(models.Model):
    pass