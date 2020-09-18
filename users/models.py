from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    klass = models.PositiveSmallIntegerField(default=0)
    imya = models.TextField(max_length=50, default='-')
    familiya = models.TextField(max_length=50, default='-')
    otchestvo = models.TextField(max_length=50, default='-')
    telefon = models.TextField(max_length=50, default='-')
    grupa = models.TextField(max_length=50, default='-')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def __str__(self):
        return self.email