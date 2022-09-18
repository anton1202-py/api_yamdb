from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, bio, password=None, role='user'):
        user = self.model(username=username,
                          email=self.normalize_email(email),
                          role=role,
                          bio=bio)
        user.set_unusable_password()
        user.save()

        return user

    def create_superuser(self, username, email, password, role='admin',
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
