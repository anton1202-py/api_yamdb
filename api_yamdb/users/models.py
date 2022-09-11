from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken


USER_ROLES = (
    ('user', 'Пользователь'),
    ('moderator', 'Модератор'),
    ('admin', 'Администратор'),
)


class UserManager(BaseUserManager):
    def create_user(self, username, email, role, bio, password=None):
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')
        user = self.model(username=username,
                          email=self.normalize_email(email),
                          role=role,
                          bio=bio)
        user.set_unusable_password()
        user.save()

        return user

    def create_superuser(self,
                         username,
                         email,
                         password,
                         role='admin',
                         bio=''):
        if password is None:
            raise TypeError('Superusers must have a password.')
        user = self.create_user(username=username,
                                email=email,
                                role=role,
                                bio=bio)
        user.password = make_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    role = models.CharField('Роль',
                            max_length=255,
                            blank=True,
                            default='user',
                            choices=USER_ROLES)
    bio = models.TextField('О себе', blank=True, default='')
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def token(self):
        return RefreshToken.for_user(self).access_token
