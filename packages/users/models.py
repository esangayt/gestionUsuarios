from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from django.db import models

from packages.users import Manager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    codregistro = models.CharField(max_length=6, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    objects = Manager.UserManager()

    #para consola
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
