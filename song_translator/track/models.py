from django.db import models


class Singer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=64)
    text = models.TextField()
    translate_text = models.TextField(blank=True)
    original_language = models.CharField(max_length=2)
    singer = models.ManyToManyField(Singer)
    owner = models.ForeignKey('auth.User', related_name='tracks', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
