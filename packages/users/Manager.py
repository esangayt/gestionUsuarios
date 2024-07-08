from django.db import models

from django.contrib.auth.models import (
    BaseUserManager
)


class UserManager(BaseUserManager, models.Manager):
    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False,False, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, True, True,True, **extra_fields)

    def _create_user(self, username, email, password, is_staff, is_superuser, is_active, **extra_fields):
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def cof_validate(self, id_user, cod_registro):
        print("id_user", id_user)
        print("cod_registro", cod_registro)
        return self.filter(id=id_user, codregistro=cod_registro).exists()