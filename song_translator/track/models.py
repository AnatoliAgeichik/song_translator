from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

from .utils import LANG_CHOICES


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class TranslatorUser(AbstractUser):
    email = models.EmailField('email address', unique=True)

    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    is_singer = models.BooleanField(default=False)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.email


class Singer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=64)
    text = models.TextField()
    original_language = models.CharField(max_length=2, choices=LANG_CHOICES, default="en")
    singer = models.ManyToManyField(Singer)
    owner = models.ForeignKey('track.TranslatorUser', related_name='tracks', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Translate(models.Model):
    track_id = models.ForeignKey('Track', related_name='translate_track', on_delete=models.CASCADE)
    text = models.TextField()
    language = models.CharField(max_length=2, choices=LANG_CHOICES, default="en")

    def __str__(self):
        return f"{self.track_id}: {self.language}"
