"""
Because we set a custom user model (used `email` replace `username`),
we have to define a custom user manager; otherwise, when we execute
`$ python manage.py createsuperuser`, it will output:
TypeError: create_superuser() missing 1 required positional argument: 'username'

References:
https://koenwoortman.com/python-django-email-as-username/
https://docs.djangoproject.com/en/dev/topics/auth/customizing/#a-full-example
"""


from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True  # add
        user.is_superuser = True  # add
        user.save(using=self._db)
        return user
