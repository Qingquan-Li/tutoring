from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .utils.my_user_manager import MyUserManager


class CustomUser(AbstractUser):
    """
    Reference: https://koenwoortman.com/python-django-email-as-username/
    """
    # username = models.CharField(
    #     _("username"),
    #     max_length=150,
    #     unique=True,
    #     help_text=_(
    #         "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
    #     ),
    #     validators=[username_validator],
    #     error_messages={
    #         "unique": _("A user with that username already exists."),
    #     },
    # )
    username = None

    # email = models.EmailField(_("email address"), blank=True)
    email = models.EmailField(_("email address"), unique=True)

    # USERNAME_FIELD = "username"
    USERNAME_FIELD = "email"

    # A list of the field names that will be prompted for
    # when creating a user via the createsuperuser management command.
    # REQUIRED_FIELDS = ["email"]
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self):
        return self.email


class CommonInfo(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    version = models.PositiveSmallIntegerField(default=0, editable=False)

    # is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    # docs.djangoproject.com/en/3.2/topics/db/models/#overriding-model-methods
    def save(self, *args, **kwargs):
        self.version = self.version + 1
        super().save(*args, **kwargs)  # Call the "real" save() method.


class Institution(models.Model):
    # docs.djangoproject.com/en/4.1/topics/db/models/#automatic-primary-key-fields
    # id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        # If you don’t set list_display, the admin site will display a single
        # column that displays the __str__() representation of each object.
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        # If you don’t set list_display, the admin site will display a single
        # column that displays the __str__() representation of each object.
        return self.name


class Profile(CommonInfo):
    user = models.OneToOneField(to=CustomUser,
                                on_delete=models.CASCADE,
                                to_field='id')
    avatar_url = models.URLField(max_length=200, blank=True, null=True)
    institution = models.ForeignKey(to=Institution,
                                    on_delete=models.CASCADE,
                                    blank=True,
                                    null=True)
    department = models.ForeignKey(to=Department,
                                   on_delete=models.CASCADE,
                                   blank=True,
                                   null=True)

    def __str__(self):
        return ''
