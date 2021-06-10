from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from .utils import LANG_CHOICES


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email


class Singer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Track(models.Model):
    track_name = models.CharField(max_length=64)
    text = models.TextField()
    original_language = models.CharField(max_length=2, choices=LANG_CHOICES, default="en")
    singer = models.ManyToManyField(Singer)
    owner = models.ForeignKey('track.User', related_name='tracks', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.track_name


class Translation(models.Model):
    track_id = models.ForeignKey('Track', related_name='translate_track', on_delete=models.CASCADE)
    text = models.TextField()
    language = models.CharField(max_length=2, choices=LANG_CHOICES, default="en")
    auto_translate = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.track_id}: {self.language}"


class Comment(models.Model):
    track_id = models.ForeignKey('Track', related_name='comment_track', on_delete=models.CASCADE)
    message = models.TextField()
    mark = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    owner = models.ForeignKey('track.User', related_name='comment_owner', null=True, on_delete=models.SET_NULL, default=1)

    def __str__(self):
        return f"{self.track_id}: {self.message[:10]}"
